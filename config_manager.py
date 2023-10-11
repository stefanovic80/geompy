import json

class ConfigurationManager:
    def __init__(self, config_file):
        self.config_file = config_file
        self.load_config()

    def load_config(self):
        try:
            with open(self.config_file, 'r') as f:
                self.config = json.load(f)
        except FileNotFoundError:
            self.config = {}

    def update_config(self, key, value):
        self.config[key] = value
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f)

    def get_config(self, key, default=None):
        return self.config.get(key, default)
