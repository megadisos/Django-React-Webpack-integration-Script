from project_creation import Project_creation
import os
class Integrator():
    def __init__(self, name):
        self.name = name
    def menu_principal(self):
        recomendations = "Before to start remember to have installed DJANGO and DJANGO REST FRAMEWORK to avoid errors"
        size = len(recomendations)+10
        print("")
        print("*"*size)
        print(" "*30 + " WELCOME TO DJANGO-REACT INTEGRATOR WITH WEBPACK")
        print("*"*size)
        print(recomendations)
        print("*"*size)
        print("Let on blank if you want keep the default")
        name = input("Project Name ("+ self.name +"): ")
        if name == "":
            name = self.name
        name = str(name)
        name = name.replace(" ","") 
        while True:
            path = input("Project Path ("+ os.getcwd() +"): ")  
            if path == "":
                path = os.getcwd()   
            try:
                os.chdir(path)
                break
            except:
                print("ERROR: The path does not exist")    
        
        new = Project_creation(name,path,size)
        new.new_project()    
        

start = Integrator("START")
start.menu_principal()     
        
        
