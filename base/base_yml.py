import yaml

def yml_file(a):
    with open("./data/" + a + ".yml", "r")as f:
        data = yaml.safe_load(f)
        return data

