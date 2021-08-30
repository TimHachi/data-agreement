import keywords
import re

def filter_text(text_dict, regular_expression):
    result = []
    for id,entry in text_dict[keywords.root].items():
        if re.search(regular_expression,entry[keywords.text]) is not None:
            result.append(id)
    return result

def filter_metadata(text_dict, metadata_field, regular_expression):
    result = []
    for id,entry in text_dict[keywords.root].items():
        if type(entry[keywords.metadata][metadata_field]) is str:
            if re.search(regular_expression,entry[keywords.metadata][metadata_field]) is not None:
                result.append(id)
    return result