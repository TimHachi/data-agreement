import keywords

def set_metadata(text_dict,ids,metadata_field,metadata_value):
    for id in ids:
        text_dict[keywords.root][id][keywords.metadata][metadata_field] = metadata_value
    return