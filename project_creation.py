from api_creation import Api_creation
import os
class Project_creation():
    def __init__(self, name,path,size):
        self.name = name
        self.path = path
        self.size = size
    def new_project(self):
        os.chdir(self.path)
        command = "django-admin startproject " + self.name
        try:
            print("*"*self.size)
            print(f"1-Creating the project {self.name}... ")
            os.system(command)
            print("The project "+self.name+" was created")
            print("*"*self.size)
            new_api = Api_creation(self.name,self.path,self.size)
            new_api.api_creation()
        except Exception as e:
            print(f"An error ocurred {e}")
       

        
