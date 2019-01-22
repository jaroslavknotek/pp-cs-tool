import os
import utils
from shutil import copyfile

import logging

logger = logging.getLogger(__name__)


def backup_locally(file_path, bck_dir_path=None):
    """
    Takes file and puts in a given directory

    :param file_path:
        path to a file to-be-backed-up
    :param bck_dir_path:
        path to directory into which the file will be backed up.
        In no path is given, directory 'backup' is created in the parent directory of file_path
    :return: None
    """

    if not bck_dir_path:
        parent = os.path.dirname(file_path)
        bck_dir_path = os.path.join(parent, "backup")

    utils.ensure_dir(bck_dir_path)
    timestamp = utils.get_timestamp()

    filename_no_ext, ext = __parse_file_name(file_path)

    new_file_name = "{}_{}{}".format(filename_no_ext, timestamp, ext)
    new_file_path = os.path.join(bck_dir_path, new_file_name)

    logger.info('backing up data')
    copyfile(file_path, new_file_path)


def __parse_file_name(file_path):
    """
    extracts file name an extension from file path

    :param file_path:
    :return: (str, str)
        returns filename and extension
    """
    filename = os.path.basename(file_path)
    split_filename = os.path.splitext(filename)
    filename_no_ext = split_filename[0]
    ext = ""
    if len(split_filename) > 1:
        # assuming the second part as an extension
        ext = split_filename[1]
    return filename_no_ext, ext
