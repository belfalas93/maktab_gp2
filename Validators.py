import re
class Validation:
    
    @staticmethod
    def correctwords(text):
        pattern=r'(fosh|bi adab|bi nezakat)'
        return re.sub(pattern,'gol',text)
        