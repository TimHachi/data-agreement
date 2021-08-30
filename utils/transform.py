import ujson
import keywords

def dict_to_text(text_dict:dict):
    return "".join([entry[keywords.text] for entry in text_dict[keywords.root].values()])

def json_to_dict(json:str):
    return ujson.loads(json)

def dict_to_json(text_dict:dict):
    return ujson.dumps(text_dict)