import os
import onedrivesdk
from onedrivesdk.helpers import GetAuthCodeServer


def download_from_root(client, destination_directory, filename):
    """
    download file from onedrive root file. Raises error if file is missing
    :param client:
        onedrive client
    :param destination_directory: str
        destination directory path
    :param filename:
        onedrive file name
    :return:
    """

    destination_path = os.path.join(destination_directory, filename)
    root_folder = client.item(drive='me', id='root').children.get()

    for f in root_folder:
        if f.name == filename:
            client.item(drive='me', id=f.id).download(destination_path)
            return

    raise ValueError("file not found")


def upload(client, file_name_local, file_name_cloud):
    """
    Upload given local file to cloud
    :param client:
        onedrive client
    :param file_name_local: str
        path to local file
    :param file_name_cloud:
        cloud path of uploaded file
    :return:
    """
    client.item(drive='me', id='root').children[file_name_cloud].upload(file_name_local)


def get_onedrive_client(client_id, client_secret):
    """
    Initializes onedrive client
    :param client_id: str
        application id
    :param client_secret: str
        client secret
    :return:
        onedrive api client
    """
    redirect_uri = 'http://localhost:8080/'
    scopes = ['wl.signin', 'wl.offline_access', 'onedrive.readwrite']

    client = onedrivesdk.get_default_client(
        client_id=client_id, scopes=scopes)

    auth_url = client.auth_provider.get_auth_url(redirect_uri)

    # this will block until we have the code
    code = GetAuthCodeServer.get_auth_code(auth_url, redirect_uri)
    client.auth_provider.authenticate(code, redirect_uri, client_secret)
    return client
