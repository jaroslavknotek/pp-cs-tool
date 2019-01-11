import os
import onedrive_api
import archiver
import backuper


def sync(dir_path, archive_pass, onedrive_config):
    """
    archives all files(not dirs) in a given location and uploads them to onedrive
    :param dir_path: str
        path to directory with files desired to be synced
    :param archive_pass:
        archive password
    :param onedrive_config: dict
        cliend id ('id) and client secret ('secret') of onedrive credentials
    :return: None

    """
    client_id = onedrive_config["id"]
    client_secret = onedrive_config["secret"]

    client = onedrive_api.get_onedrive_client(client_id, client_secret)
    archive_name = os.path.basename(dir_path)
    archive_path = archiver.archive_files(dir_path, archive_name, archive_pass)

    archive_cloud_name = archive_name + ".zip"
    onedrive_api.upload(client, archive_path, archive_cloud_name)
    backuper.backup_locally(archive_path)
