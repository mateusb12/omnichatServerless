import os

from dotenv import load_dotenv
from google.oauth2 import service_account

from references.path_reference import getSdkFolderPath


def load_cloud_credentials():
    load_dotenv()
    key_path = str(getSdkFolderPath() / "middleware_omnichat.json")
    credentials = service_account.Credentials.from_service_account_file(
        key_path,
        scopes=["https://www.googleapis.com/auth/cloud-platform"],
    )
    # Set the credentials in the environment variables
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = key_path


def __main():
    load_cloud_credentials()
    print(os.environ.get("GOOGLE_APPLICATION_CREDENTIALS"))


if __name__ == '__main__':
    __main()
