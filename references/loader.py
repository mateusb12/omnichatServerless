import json

from references.path_reference import getSpeisekartePath


def loadSpeisekarte() -> dict:
    path = getSpeisekartePath()
    with path.open(encoding='utf-8') as file:
        return json.load(file)
