import spacy
   

class Tokenizer:
    def __init__(self,language:str,add_sos:bool=True,add_eos:bool=True,lowercase:bool=True):
        try:
            self.tokenizer = spacy.load(language).tokenizer
        except OSError:
            print(f"Downloading {language} model...")
            spacy.cli.download(language)
            self.tokenizer = spacy.load(language).tokenizer

        self.add_sos = add_sos
        self.add_eos = add_eos
        self.lowercase = lowercase
    
    def tokenize(self,text:str):
        if self.lowercase:
            text = text.lower()
        tokens = [tok.text for tok in self.tokenizer(text)]
        if self.add_sos:
            tokens = ["<sos>"] + tokens
        if self.add_eos:
            tokens = tokens + ["<eos>"]
        return tokens
    
if __name__=="__main__":

    german_tokenizer = Tokenizer(language="de_core_news_sm")
    english_tokenizer = Tokenizer(language="en_core_web_sm")
    german_text = "Hallo Welt!"
    english_text = "Hello World!"

    german_tokens = german_tokenizer.tokenize(german_text)
    english_tokens = english_tokenizer.tokenize(english_text)

    print(f"German Tokens: {german_tokens}\nEnglish Tokens: {english_tokens}")

