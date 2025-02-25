"""
check_drive.py

Checks the google drive for files not currently accounted for.

TODO: Needs to be updated avoid having unecessary constants at the top of the file.
"""

import os
import json
from typing import List, Dict
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from google.oauth2.service_account import Credentials

# Constants
SCOPES = ["https://www.googleapis.com/auth/drive.readonly"]
FOLDER_ID = "YOUR_GOOGLE_DRIVE_FOLDER_ID"  # Replace with actual folder ID
KNOWN_FILES_JSON = "known_files.json"
ARTIFACT_FILE = "new_files.json"
SERVICE_ACCOUNT_FILE = "service_account.json"  # GitHub will inject this securely


def authenticate_gdrive() -> build:
    """
    Authenticate with Google Drive using a service account.

    Returns:
        drive_service: Authenticated Google Drive service instance.
    """
    credentials = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    return build("drive", "v3", credentials=credentials)


def fetch_google_sheets(drive_service) -> List[Dict[str, str]]:
    """
    Fetch all Google Sheets files in the specified Google Drive folder.

    Args:
        drive_service: Authenticated Google Drive service instance.

    Returns:
        List of dictionaries containing file ID and name.
    """
    query = f"'{FOLDER_ID}' in parents and mimeType='application/vnd.google-apps.spreadsheet'"
    response = drive_service.files().list(q=query, fields="files(id, name)").execute()

    return response.get("files", [])


def load_known_files() -> List[str]:
    """
    Load the list of known files from a local JSON file.

    Returns:
        List of known file IDs.
    """
    if os.path.exists(KNOWN_FILES_JSON):
        with open(KNOWN_FILES_JSON, "r", encoding="utf-8") as file:
            return json.load(file).get("known_files", [])
    return []


def save_new_files(new_files: List[Dict[str, str]]) -> None:
    """
    Save newly detected files to a JSON file.

    Args:
        new_files: List of new file metadata.
    """
    with open(ARTIFACT_FILE, "w", encoding="utf-8") as file:
        json.dump({"new_files": new_files}, file, indent=4)


def update_known_files(known_files: List[str], new_files: List[Dict[str, str]]) -> None:
    """
    Update the list of known files by appending new ones.

    Args:
        known_files: List of previously known file IDs.
        new_files: List of newly found files.
    """
    known_files.extend([file["id"] for file in new_files])
    with open(KNOWN_FILES_JSON, "w", encoding="utf-8") as file:
        json.dump({"known_files": known_files}, file, indent=4)


def main() -> None:
    """
    Main execution function:
    - Fetches Google Sheets files.
    - Compares against known files.
    - Saves new files as an artifact.
    """
    drive_service = authenticate_gdrive()
    known_files = load_known_files()
    current_files = fetch_google_sheets(drive_service)

    new_files = [file for file in current_files if file["id"] not in known_files]

    if new_files:
        print(f"Found {len(new_files)} new file(s). Saving to artifact...")
        save_new_files(new_files)
        update_known_files(known_files, new_files)
    else:
        print("No new files detected.")


if __name__ == "__main__":
    main()

