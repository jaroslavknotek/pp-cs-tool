import unittest
import python.src.onedrive_api as onedrive_api
from unittest.mock import MagicMock
import os


class OneDriveCase(unittest.TestCase):
    def test_download_from_root_file_does_not_exist(self):
        # arrange
        od_client = MagicMock()
        mock_item = MagicMock()
        mock_file = MagicMock()
        mock_file.name = "foo.fi"
        mock_file.id = 2345
        mock_item.children.get.return_value = [mock_file]

        od_client.item.return_value = mock_item

        destination_directory = "foo/bar/dir"

        # act
        onedrive_api.download_from_root(od_client, destination_directory, "foo.fi")
        # assert
        mock_item.download.assert_called_with(os.path.join("foo/bar/dir", "foo.fi"))

    def test_download_from_root_file(self):
        # arrange
        od_client = MagicMock()
        mock_item = MagicMock()
        mock_file = MagicMock()
        mock_file.name = "foo.fi"
        mock_item.children.get.return_value = [mock_file]

        od_client.item.return_value = mock_item

        destination_directory = "foo/bar/dir"

        # act
        with self.assertRaises(Exception) as context:
            onedrive_api.download_from_root(od_client, destination_directory, "file.fi")
        # assert
        self.assertTrue('file not found' in str(context.exception), msg="file should not be found")


if __name__ == '__main__':
    unittest.main()
