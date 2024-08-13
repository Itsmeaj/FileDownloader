# FileDownloader

This project allows you to download files from Google Drive by specifying their names. It uses the `pydrive2` library for authentication and file handling.

## Features
- Authenticate with Google Drive using OAuth 2.0.
- Download files from Google Drive by specifying their names.
- Automatically searches for files in your Google Drive and downloads them to your local machine.

## Prerequisites
- Python 3.6 or higher
- pydrive2 library
- Google Drive API enabled
- client_secrets.json file for OAuth 2.0 authentication

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/your-repository/FileDownloader.git
    cd FileDownloader
    ```

2. **Create a Virtual Environment (Optional but recommended)**:
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    ```

3. **Install Required Packages**:
    ```bash
    pip install pydrive2
    ```

## How to Create `client_secrets.json`

1. **Go to Google Cloud Console**:
   - Open [Google Cloud Console](https://console.cloud.google.com/). Log into your account.

2. **Create a Project**:
   - click on **New Project** and provide a name.

3. **Enable Google Drive API**:
   - In the navigation menu, go to **APIs & Services > Library**.
   - Search for **Google Drive API** and click **Enable**.

4. **Create OAuth 2.0 Credentials**:
   - Navigate to **APIs & Services > Credentials**.
   - Click on **Create Credentials** and select **OAuth 2.0 Client ID**.
   - If prompted, configure the OAuth consent screen by filling in the required details like app name and email.
   - For **Application type**, select **Desktop app**.
   - After creating the credentials, click **Download JSON** to download the `client_secrets.json` file.

5. **Place the `client_secrets.json` File**:
   - Save the `client_secrets.json` file in the root directory of your project (where `file_downloader.py` is located).

## How to Assign Test Users

If your app is in development and hasn't been verified by Google, you'll need to add test users:

1. **Go to OAuth Consent Screen**:
   - Navigate to **APIs & Services > OAuth consent screen** in the Google Cloud Console.

2. **Add Test Users**:
   - Scroll down to the "Test users" section.
   - Click **Add users** and enter the email addresses of the users you want to add as testers.
   - Save the changes.

## Running the Script

To download a file from Google Drive, follow these steps:

1. **Make sure `client_secrets.json` is in the root directory of the project.**

2. **Run the script**:
    ```bash
    python file_downloader.py --file_name "your_file_name.ext" --download_path "C:\path\to\save"
    ```

   Replace `"your_file_name.ext"` with the name of the file you want to download and `"C:\path\to\save"` with the directory where you want to save the downloaded file.

### Example

To download a file named `report.pdf` and save it in `C:\Users\YourName\Downloads`, run:
User might have to manually authenticate by clicking confirm as google has strong way of authenticating users.
after selecting the account and clicking on confirm, the file will be downloaded.

```bash
python file_downloader.py --file_name "report.pdf" --download_path "C:\Users\YourName\Downloads"
