import tomllib

def config_reader(config_path:str):
    with open(config_path,"rb") as f:
        config = tomllib.load(f)
        return config