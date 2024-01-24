class MockRequest:
    def __init__(self, path, method, headers=None, json_data=None):
        self.path = path
        self.method = method
        self.headers = headers or {}
        self.json = json_data

    def get_json(self, force=False, silent=False, cache=True):
        return self.json
