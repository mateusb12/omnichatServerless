from typing import Any
from firebase_admin import db
from firebaseAuthentication.abstraction.abstract_connection import AbstractFirebaseConnection
from firebaseAuthentication.sdk_auth.firebase_sdk_auth import get_firebase_app
from utils.patterns import singleton


@singleton
class FirebaseSDKConnection(AbstractFirebaseConnection):
    def __init__(self):
        """ FirebaseConnection is a singleton class that provides mechanisms for interacting with
        Firebase realtime database."""
        self.app = get_firebase_app()
        self.connection = db.reference('/', app=self.app)

    def changeDatabaseConnection(self, path: str) -> db.reference:
        """Change the current active reference to another in Firebase."""
        self.connection = db.reference(f'/{path}', app=self.app)

    def readData(self, path: str = None) -> db.reference:
        """Reads and returns data from Firebase at the specified path."""
        ref = self.connection.child(path) if path is not None else self.connection
        return ref.get()

    def getValue(self, path: str) -> Any:
        """Get a value from Firebase at the specified path."""
        return self.readData(path)

    def setValue(self, path: str, value: Any) -> bool:
        """Set a value in Firebase at the specified path."""
        self.connection.child(path).set(value)
        return True

    def writeData(self, path: str = None, data: dict = None) -> bool:
        """Writes data to Firebase at the specified path."""
        if data is None:
            data = {"dummyData": 5}
        ref = self.connection.child(path) if path is not None else self.connection
        ref.push(data)
        return True

    def writeDataWithoutUniqueId(self, path: str = None, data: dict = None) -> bool:
        """Writes data to Firebase at the specified path."""
        if data is None:
            data = {"dummyData": 5}

        # If a path is provided, write data to that path.
        # If no path is provided, write data to the root.
        ref = self.connection.child(path) if path else self.connection

        # Use set method instead of push to avoid Firebase's unique ID generation.
        ref.set(data)
        return True

    def overWriteData(self, path: str = None, data=None) -> bool:
        """Overwrites data at the specified path in Firebase."""
        if data is None:
            data = {"dummyData": 5}
        ref = self.connection.child(path) if path is not None else self.connection
        ref.set(data)
        return True

    def deleteData(self, path: str, data=None) -> bool:
        """Deletes data at the specified path in Firebase."""

        # If only path is provided, we assume it's the direct reference to the data to delete
        if data is None:
            ref = self.connection.child(path)
            ref.delete()
            return True

        # If data is also provided, we need to find its unique ID first
        data_id = self.getUniqueIdByData(path, data)
        if data_id is None:
            raise ValueError("Cannot find unique ID for provided data")

        ref = self.connection.child(path)
        data_ref = ref.child(data_id)
        data_ref.delete()
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
    fc = FirebaseSDKConnection()
    data = fc.readData("users")
    print(data)
    return


if __name__ == '__main__':
    __main()
