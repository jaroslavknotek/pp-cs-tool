import os
import onedrive_api
import archiver
import backuper

import logging

logger = logging.getLogger(__name__)


def sync(dir_path, archive_pass, client_id, client_secret):
    """
    archives all files(not dirs) in a given location and uploads them to onedrive
    :param dir_path: str
        path to directory with files desired to be synced
    :param archive_pass:
        archive password
    :param client_id:
        one drive client id
    :param client_secret:
        one drive secret
    :return: None

    """

    logger.info('synchronizing data to one drive (not downloading yet)')
    client = onedrive_api.get_onedrive_client(client_id, client_secret)
    archive_name = os.path.basename(dir_path)
    archive_path = archiver.archive_files(dir_path, archive_name, archive_pass)

    archive_cloud_name = archive_name + ".zip"
    onedrive_api.upload(client, archive_path, archive_cloud_name)
    backuper.backup_locally(archive_path)
