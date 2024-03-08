import Story
class Writer:

    def __init__(self , name , email):
        self.name = name
        self.email = email
        self.stories=[]

    def add_story(self,title):
        
        self.stories.append(Story.Stories(title,self))


