import yaml

with open("src/config.yml", "r") as file:
    config = yaml.load(file, Loader=yaml.FullLoader)
    
token = config['token']