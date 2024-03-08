import os

class MyManager:   
    directory = 'temp_stories'
    parent_dir = os.getcwd()
    i=1
    
    def __init__(self, name, method):
        self.name = name
        self.method= method

    def __enter__(self):
        self.file = open(self.name , self.method) 
        return self.file
    
    def __exit__(self, type, value, traceback):
        
        path = os.path.join(self.parent_dir , self.directory)
        if not os.path.exists(path):
            os.mkdir(path)
        
        name=f'temp{self.i}.txt'
       
        temp_path=os.path.join(path , name)
        with open(temp_path,'w') as f:
            f.write(self.file.read())
        self.file.close()


with MyManager('C:/Users/navid/OneDrive/Desktop/story.txt','r') as file:
    pass





# class UploaderContexManager:
#     parent_dir = os.getcwd()
#     temp_directory = 'temp_stories'


#     @classmethod
#     def data_reader(cls,directory):

#         try:
#             with open(directory , 'r') as s , open(os.path.join(cls.parent_dir , cls.temp_dir) , 'w') as temp:
                
#                 temp.writelines(s.readlines())
#         except:
#             print('Error...')
# a= open(file , method)
# a.read(file)
# a.close()
# UploaderContexManager.data_reader('Stories.txt')