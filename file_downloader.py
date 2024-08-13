import os
import argparse
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive


def authenticate_drive():
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()  # Create local webserver and handle authentication.
    return GoogleDrive(gauth)


def download_file_by_name(file_name, download_path):
    drive = authenticate_drive()

    # Search for the file by name in the entire Google Drive
    query = f"title='{file_name}' and trashed=false"
    file_list = drive.ListFile({'q': query}).GetList()

    if len(file_list) == 0:
        print(f"No file found with the name '{file_name}'.")
        return
    elif len(file_list) > 1:
        print(f"Multiple files found with the name '{file_name}'. Please specify the correct one.")
        for idx, file in enumerate(file_list):
            print(f"{idx + 1}. {file['title']} (ID: {file['id']})")
        return

    # Download the first (and presumably only) matching file
    file = file_list[0]
    file_path = os.path.join(download_path, file['title'])
    print(f"Downloading '{file['title']}' to '{file_path}'...")
    file.GetContentFile(file_path)
    print(f"Downloaded '{file['title']}' successfully.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download a file from Google Drive by name.")
    parser.add_argument('--file_name', required=True, help="The name of the file to download.")
    parser.add_argument('--download_path', default=".", help="The local directory to save the downloaded file.")

    args = parser.parse_args()

    download_file_by_name(args.file_name, args.download_path)
