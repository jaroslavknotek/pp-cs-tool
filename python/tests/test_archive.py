import unittest
import python.src.utils as utils
import os
import python.src.archiver as archiver
import python.src.backuper as backuper
import python.src.synchronizer as synchronizer
import tempfile
import shutil
import mock
from unittest.mock import Mock


class ArchiveTestCase(unittest.TestCase):

    def setUp(self):
        # Create a temporary directory
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        # Remove the directory after the test
        shutil.rmtree(self.test_dir)

    @mock.patch('python.src.synchronizer.backuper')
    @mock.patch('python.src.synchronizer.archiver')
    @mock.patch('python.src.synchronizer.onedrive_api')
    def sync(self, mock_onedrive_api, mock_archiver, mock_backuper):
        # arrange
        config = {"id": "123", "secret": "password"}
        dir_path = os.path.join(self.test_dir, "data")

        client = Mock()
        mock_onedrive_api.get_onedrive_client.return_value = client

        archive_path = os.path.join(self.dir_path, "archived", "ar")
        mock_archiver.archive_files.return_value = archive_path

        # act
        synchronizer.sync(self.test_dir, "1234_pass", config)

        # assert
        mock_onedrive_api.get_onedrive_client.assert_called_with("123", "password")
        mock_onedrive_api.upload.assert_called_with(client, archive_path, )
        mock_archiver.archive_files.assert_called_with(dir_path, "ar", "1234_pass")
        mock_backuper.backup_locally.assert_called_with(archive_path)

    @mock.patch('python.src.utils.os')
    def test_ensure_dir(self, mock_os):
        test_dir_path = os.path.join(self.test_dir, "dir_test")

        utils.ensure_dir(test_dir_path)
        mock_os.makedirs.assert_called_with(test_dir_path)

    def test_ensure_dir_invalid_dir_name(self):
        error_msg = "directory with wrong name was created"
        with self.assertRaises(Exception) as context:
            utils.ensure_dir("")

        self.assertTrue('invalid directory name' in str(context.exception), msg=error_msg)

        with self.assertRaises(Exception) as context:
            utils.ensure_dir(123)

        self.assertTrue('invalid directory name' in str(context.exception), msg=error_msg)

    @mock.patch('python.src.archiver.pyminizip')
    @mock.patch('python.src.archiver.utils')
    @mock.patch('python.src.archiver.os.path')
    @mock.patch('python.src.archiver.os')
    def test_archive_files(self, mock_os, mock_archiver_os_path, mock_utils, mock_pyminizip):
        # arrange
        mock_os.listdir.return_value = ["file1", "file2"]
        mock_archiver_os_path.isfile.return_value = True

        def side_effect(arg1, arg2):
            return os.path.join(arg1, arg2)

        mock_archiver_os_path.join.side_effect = side_effect

        # act
        archive_path = archiver.archive_files(self.test_dir, "some_name", "my_pass")

        # assert
        mock_utils.ensure_dir.assert_called_with(os.path.join(self.test_dir, "archived"))
        mock_pyminizip.compress_multiple.assert_called_with(
            [self.test_dir + os.sep + 'file1',
             self.test_dir + os.sep + 'file2'],
            ['data', 'data'],
            self.test_dir + os.sep + 'archived\\some_name.zip',
            "my_pass", 5)

        self.assertEqual(os.path.join(self.test_dir, "archived", "some_name.zip"), archive_path)

    @mock.patch('python.src.backuper.utils')
    @mock.patch('python.src.backuper.copyfile')
    def test_backup_locally_no_dest(self, mock_copyfile, mock_utils):
        # arrange
        archive_path = os.path.join(self.test_dir, "my_archive.zip")
        backup_path = os.path.join(self.test_dir, "different_backup")
        mock_utils.get_timestamp.return_value = "20190110T152817100"
        # act
        backuper.backup_locally(archive_path)
        backuper.backup_locally(archive_path, backup_path)
        # assert

        expected_backup_path = os.path.join(self.test_dir, "backup", "my_archive_20190110T152817100.zip")
        mock_copyfile.assert_any_call(archive_path, expected_backup_path)

        expected_backup_path = os.path.join(self.test_dir, "different_backup", "my_archive_20190110T152817100.zip")
        mock_copyfile.assert_called_with(archive_path, expected_backup_path)


if __name__ == '__main__':
    unittest.main()
