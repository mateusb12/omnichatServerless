import os

from dotenv import load_dotenv
from firebase_admin import credentials, initialize_app, App

from authentication.sdk_auth.sdk_dict import getSdkDict

load_dotenv()


def __getFirebaseCredentials() -> credentials.Certificate:
    firebase_credentials = getSdkDict()
    key = firebase_credentials["private_key"]
    key = key.replace("-----BEGIN PRIVATE KEY-----", "").replace("-----END PRIVATE KEY-----", "").strip()
    key = f"-----BEGIN PRIVATE KEY-----\n{key}\n-----END PRIVATE KEY-----"
    firebase_credentials["private_key"] = key
    return credentials.Certificate(firebase_credentials)


def __get_database_url() -> str:
    return os.environ["FIREBASE_DATABASE_URL"]


def get_firebase_app() -> App:
    certificate = __getFirebaseCredentials()
    database_url = __get_database_url()
    return initialize_app(certificate, {"databaseURL": database_url})


def __main():
    app = get_firebase_app()
    return


if __name__ == '__main__':
    __main()