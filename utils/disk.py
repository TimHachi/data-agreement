def read_json_from_file (path:str):
    return open(path, "r").read()

def save_dict_to_file(text_dict:dict,path:str):
    with open(path, "w", errors="replace") as f:
        f.write(transform.dict_to_json(text_dict))

def save_json_to_file (json:str,path:str):
    with open(path, "w", errors = "replace") as f:
        f.write(json)