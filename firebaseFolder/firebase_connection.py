import os
import firebase_admin
from dotenv import load_dotenv
from firebase_admin import credentials, db
from references.path_reference import getFirebaseSDKPath
from utils.patterns import singleton


def getFirebaseCredentials():
    load_dotenv()
    print(f"ENVIRONMENT VARIABLES: {list(os.environ)}")
    firebase_credentials = {
        "type": os.environ["FIREBASE_SDK_TYPE"],
        "project_id": os.environ["FIREBASE_SDK_PROJECT_ID"],
        "private_key_id": os.environ["FIREBASE_SDK_PRIVATE_KEY_ID"],
        "private_key": os.environ["FIREBASE_SDK_PRIVATE_KEY"],
        "client_email": os.environ["FIREBASE_SDK_CLIENT_EMAIL"],
        "client_id": os.environ["FIREBASE_SDK_CLIENT_ID"],
        "auth_uri": os.environ["FIREBASE_SDK_AUTH_URI"],
        "token_uri": os.environ["FIREBASE_SDK_TOKEN_URI"],
        "auth_provider_x509_cert_url": os.environ["FIREBASE_SDK_AUTH_PROVIDER_X509_CERT_URL"],
        "client_x509_cert_url": os.environ["FIREBASE_SDK_CLIENT_X509_CERT_URL"]
    }
    key = firebase_credentials["private_key"]
    key = key.replace("-----BEGIN PRIVATE KEY-----", "").replace("-----END PRIVATE KEY-----", "").strip()
    key = f"-----BEGIN PRIVATE KEY-----\n{key}\n-----END PRIVATE KEY-----"
    firebase_credentials["private_key"] = key
    return credentials.Certificate(firebase_credentials)


@singleton
class FirebaseConnection:
    def __init__(self):
        """ FirebaseConnection is a singleton class that provides mechanisms for interacting with
        Firebase realtime database."""
        load_dotenv()
        cred = getFirebaseCredentials()
        self.app = firebase_admin.initialize_app(cred, {"databaseURL": os.getenv("FIREBASE_DATABASE_URL")})
        self.connection = db.reference('/', app=self.app)

    def changeDatabaseConnection(self, path: str) -> db.reference:
        """Change the current active reference to another in Firebase."""
        self.connection = db.reference(f'/{path}', app=self.app)

    def readData(self, path: str = None) -> db.reference:
        """Reads and returns data from Firebase at the specified path."""
        ref = self.connection.child(path) if path is not None else self.connection
        return ref.get()

    def writeData(self, path: str = None, data=None) -> bool:
        """Writes data to Firebase at the specified path."""
        if data is None:
            data = {"dummyData": 5}
        ref = self.connection.child(path) if path is not None else self.connection
        ref.push(data)
        return True

    def overWriteData(self, path: str = None, data=None) -> bool:
        """Overwrites data at the specified path in Firebase."""
        if data is None:
            data = {"dummyData": 5}
        ref = self.connection.child(path) if path is not None else self.connection
        ref.set(data)
        return True

    def deleteData(self, path: str = None, data=None) -> bool:
        """Deletes data at the specified path in Firebase."""
        user_id = self.getUniqueIdByData(path, data)
        if user_id is None:
            raise ValueError("User ID cannot be None")
        ref = self.connection.child(path) if path is not None else self.connection
        user_ref = ref.child(user_id)
        user_ref.delete()
        return True

    def deleteAllData(self) -> bool:
        """Deletes all data at the root of the Firebase Database."""
        ref = self.connection
        ref.delete()
        return True

    def getUniqueIdByData(self, path: str = None, data=None) -> str:
        """Returns the generated unique key for that data."""
        if data is None:
            raise ValueError("Data cannot be None")
        ref = self.connection.child(path) if path is not None else self.connection
        return ref.push(data).key


def __main():
    fc = FirebaseConnection()
    data = fc.readData("users")
    return


if __name__ == '__main__':
    __main()
