import json


def get_app_config():
    with open("settings.json") as file:
        app_config = json.load(file)

    return app_config
