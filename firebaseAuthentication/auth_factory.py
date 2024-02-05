from firebaseAuthentication.http_auth.firebase_http_connection import FirebaseHTTPConnection
from firebaseAuthentication.sdk_auth.firebase_sdk_connection import FirebaseSDKConnection


class FirebaseConnectionFactory:
    @staticmethod
    def create_connection(connection_type: str) -> object:
        if connection_type == "SDK":
            return FirebaseSDKConnection()
        elif connection_type == "HTTP":
            return FirebaseHTTPConnection()
        else:
            raise ValueError(f"[{connection_type}] unknown connection type. Only known types are 'SDK' and 'HTTP'.")


def __main():
    fcc = FirebaseConnectionFactory()
    sdk_connection = fcc.create_connection("SDK")
    return


if __name__ == '__main__':
    __main()
