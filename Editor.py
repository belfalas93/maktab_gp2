import os
import re
from Validators import Validation

class FilterEditorHandler:
    directory = 'final_stories'
    parent_dir = os.getcwd()

    def __enter__(self):
        self.file = open('temp_stories/temp1.txt' , 'r',-1,'utf-8')
        print(Validation.correctwords(self.file.read()))
        return self.file
    
    def __exit__(self, type, value, traceback):
        path = os.path.join(self.parent_dir , self.directory)
        if not os.path.exists(path):
            os.mkdir(path)
        
        name='final_stories.txt'
        temp_path=os.path.join(path , name)
        with open(temp_path,'w') as f:
            
            f.write(self.file.read())
        
        self.file.close()
        os.remove('temp_stories/temp1.txt')
        


with FilterEditorHandler() as file:
    pass