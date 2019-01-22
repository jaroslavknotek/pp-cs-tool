import os
import pyminizip
import utils
import logging

logger = logging.getLogger(__name__)


def archive_files(dir_path, archive_name, password):
    """
    Archives all files(no dirs) in a given directory.
    Stores the archive in a 'archive' subdir
    :param dir_path: str
        path to directory with files
    :param archive_name: str
        name of the archive without path. Zip extension is added if missing
    :param password: str
        archive password
    :return: str
        path
    """
    files_to_archive = [os.path.join(dir_path, f) for f in os.listdir(dir_path) if
                        os.path.isfile(os.path.join(dir_path, f))]
    # prefix is a literal
    file_prefix = "data"
    file_prefixes = [file_prefix for _ in files_to_archive]

    if not str.endswith(archive_name, ".zip"):
        archive_name = archive_name + ".zip"

    archive_dir_name = "archived"
    archive_dir = os.path.join(dir_path, archive_dir_name)
    utils.ensure_dir(archive_dir)
    archive_path = os.path.join(archive_dir, archive_name)

    logger.info('archiving files{}'.format(files_to_archive))
    pyminizip.compress_multiple(files_to_archive, file_prefixes, archive_path, password, 5)
    return archive_path


def extract(archive_path, password, target_path="."):
    """
    Extracts archive using password to given target location
    :param archive_path: str
        path to archive
    :param password: str
        archive password
    :param target_path: str
        target path
    :return:
        path where the archive was extracted
    """
    logger.info('extracting data from {}'.format(archive_path))
    pyminizip.uncompress(archive_path, password, target_path, 0)
    return target_path
