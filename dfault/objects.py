
class Dfault(object):
    default_config = None

    def __init__(self, default_config):
        self.default_config = default_config

    def get(self, name, default_name):
        self.default_config
        try:
            return self.default_config[name]
        except:
            return default_name


