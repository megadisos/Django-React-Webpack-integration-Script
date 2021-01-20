import os
from shutil import copyfile,copy
import shutil
class ReactAppCreation:
    def __init__(self,size,path,name):
        self.size = size
        self.path = path
        self.name = name
    def folder_creation(self):
        FOLDER_TO_CREATE = ["templates","static","src"]
        FOLDER_AT_SRC = ["css","frontend","images","components"]
        os.chdir(os.path.join(self.path,self.name))
        print(f" current path {os.getcwd()}")
        os.system("python manage.py startapp frontend")
        os.chdir(os.path.join(os.getcwd(),"frontend"))
        print("3- Creating the FrontEnd Folders ...")
        for folder in FOLDER_TO_CREATE:
            os.mkdir(os.path.join(os.getcwd(),folder))
        os.chdir(os.path.join(os.getcwd(),"src"))    
        for folder in FOLDER_AT_SRC:
            os.mkdir(os.path.join(os.getcwd(),folder))   
        os.chdir(os.path.join(self.path,self.name,"frontend","templates"))   
        os.mkdir(os.path.join(os.getcwd(),"frontend"))
        print("The folder structure was created.")  
        print("*"*self.size)

    def react_project_creation(self):
        ct = 1
        os.chdir(os.path.join(self.path,self.name,"frontend"))
        print("4- Creating react project and dependencies... ")
        COMMANDS = {"npm init -y":"initializing project ..",
                    "npm i webpack webpack-cli --save-dev":"Webpack",
                    "npm i @babel/core babel-loader @babel/preset-env @babel/preset-react --save--dev":"Babel",
                    "npm i react react-dom --save-dev":"React",
                    "npm install @material-ui/core":"Material UI",
                    "npm install @babel/plugin-proposal-class-properties":"Babel Plugins",
                    "npm install react-router-dom":"Router Dom",
                    "npm install @material-ui/icons":"Icons"}

        for cmd,tit in COMMANDS.items():
            if ct == 1:
                print(f"4.{ct}- {tit} :")
                print("")
            else:
                print(f"4.{ct}- installing {tit} ... :")  
                print("")  
            os.system(cmd)
            ct += 1
        print("The Frontend installation was done.")    
        print("*"*self.size)
    
    def files_configuration(self):
        files_path = os.path.dirname(os.path.abspath(__file__))
        self.folder_creation()
        self.react_project_creation()
        FILES_TO_COPY = ["babel.config.json","webpack.config.js"]
        print("5- Configuring react files ...")
      
        for files in FILES_TO_COPY:
           shutil.copy(os.path.join(files_path,"files",files),
                     os.path.join(self.path,self.name,"frontend"))

        shutil.copy(os.path.join(files_path,"files","index.html"),
                    os.path.join(self.path,"frontend","templates","frontend"))  
        shutil.copy(os.path.join(files_path,"files","urls.py.fe"),
                    os.path.join(self.path,"frontend","urls.py"))                       
        packagejs_path = os.path.join(self.path,self.name,"frontend","package.json")       

        with open(packagejs_path,"r") as file:
            data = file.readlines()

        for dt in data:
            if '"test"' in dt:
                location = data.index(dt)  
        data[location] = '\t\t"dev": "webpack --mode development --watch",\n'    
        data.insert(location+1,'\t\t"build": "webpack --mode production"\n')   
        with open(packagejs_path,"w") as file:
            file.writelines(data)
        with open(os.path.join(self.path,self.name,"frontend","src","index.js"), "w") as file:
            file.writelines(['import App from "./components/App";\n'])
        
        ## Django Files
        views_path = os.path.join(self.path,self.name,"frontend","views.py")
        data = ["from django.shortcuts import render\n","def index(request, *args,**kwargs):","\treturn render(request,'frontend/index.html')"]
        with open(views_path, "r") as file:
            file.writelines(data)     


        print("The configuration was done")         
        print("*"*self.size)    
        
     


