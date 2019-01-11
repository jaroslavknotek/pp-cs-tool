import os
import errno
import datetime


def ensure_dir(directory):
    """
    ensures that directory is created
    :param directory: str
        directory to be created
    :return:
    """

    if type(directory) is not str or directory == "":
        raise Exception("invalid directory name")

    try:
        os.makedirs(directory)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise


def get_timestamp():
    return datetime.datetime.utcnow().strftime('%Y%m%dT%H%M%S%f')[:-3]
