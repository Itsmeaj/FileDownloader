import unittest
import os
from unittest.mock import patch, MagicMock
from file_downloader import download_file_by_name


class TestFileDownloader(unittest.TestCase):

    @patch('file_downloader.authenticate_drive')
    def test_download_existing_file(self, mock_authenticate_drive):
        """
        Test that an existing file is downloaded correctly.
        """
        # Set up the mock Google Drive instance
        mock_drive = MagicMock()
        mock_file = MagicMock()
        mock_file['title'] = "example_file.pdf"
        mock_file.GetContentFile = MagicMock()
        mock_drive.ListFile().GetList.return_value = [mock_file]
        mock_authenticate_drive.return_value = mock_drive

        # Perform the download
        download_path = "./"
        download_file_by_name("example_file.pdf", download_path)

        # Assert that the file was downloaded to the correct path
        mock_file.GetContentFile.assert_called_once_with(os.path.join(download_path, "example_file.pdf"))

    @patch('file_downloader.authenticate_drive')
    def test_file_not_found(self, mock_authenticate_drive):
        """
        Test that the function exits when the file is not found.
        """
        # Mock Google Drive with no files
        mock_drive = MagicMock()
        mock_drive.ListFile().GetList.return_value = []
        mock_authenticate_drive.return_value = mock_drive

        # Verify that a SystemExit exception is raised
        with self.assertRaises(SystemExit) as cm:
            download_file_by_name("non_existing_file.pdf", "./")
        self.assertEqual(cm.exception.code, 1)

    @patch('file_downloader.authenticate_drive')
    def test_multiple_files_found(self, mock_authenticate_drive):
        """
        Test that the function exits when multiple files with the same name are found.
        """
        # Mock Google Drive with multiple files found
        mock_drive = MagicMock()
        mock_file1 = MagicMock()
        mock_file1['title'] = "example_file.pdf"
        mock_file2 = MagicMock()
        mock_file2['title'] = "example_file.pdf"
        mock_drive.ListFile().GetList.return_value = [mock_file1, mock_file2]
        mock_authenticate_drive.return_value = mock_drive

        # Verify that a SystemExit exception is raised
        with self.assertRaises(SystemExit) as cm:
            download_file_by_name("example_file.pdf", "./")
        self.assertEqual(cm.exception.code, 1)

    @patch('file_downloader.authenticate_drive')
    def test_invalid_download_path(self, mock_authenticate_drive):
        """
        Test that the function raises an OSError when given an invalid download path.
        """
        # Mock Google Drive with a single file
        mock_drive = MagicMock()
        mock_file = MagicMock()
        mock_file['title'] = "example_file.pdf"
        mock_file.GetContentFile = MagicMock()
        mock_drive.ListFile().GetList.return_value = [mock_file]
        mock_authenticate_drive.return_value = mock_drive

        # Attempt to download to an invalid path
        invalid_path = "/invalid_path/that/does/not/exist/"
        with self.assertRaises(OSError):
            download_file_by_name("example_file.pdf", invalid_path)

    @patch('file_downloader.authenticate_drive')
    def test_no_files_in_drive(self, mock_authenticate_drive):
        """
        Test that the function exits when no files are found in Google Drive.
        """
        # Mock Google Drive with no files at all
        mock_drive = MagicMock()
        mock_drive.ListFile().GetList.return_value = []
        mock_authenticate_drive.return_value = mock_drive

        # Verify that a SystemExit exception is raised
        with self.assertRaises(SystemExit) as cm:
            download_file_by_name("any_file.pdf", "./")
        self.assertEqual(cm.exception.code, 1)


if __name__ == '__main__':
    unittest.main()
