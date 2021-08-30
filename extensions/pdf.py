import fitz
import keywords

def create_dict_from_pdf(path):
    doc = fitz.open(path)
    text_dict = {}
    text_dict[keywords.root] = {}
    i = 0
    for page in doc:
        text = page.getText("words")
        for x0,y0,x1,y1,word,block_no,line_no,word_no in text:
            text_dict[keywords.root][str(i)] = [keywords.text:str(word),keywords.metadata:{"bbox":[str(x0),str(y0),str(x1),str(y1)],"block_no":str(block_no),"line_no":str(line_no),"word_no":str(word_no),"page_no":page.number}]