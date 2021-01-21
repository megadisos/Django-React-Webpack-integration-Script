import os
from shutil import copyfile,copy
import shutil
from integration_files.aditional_tasks import read_file, write_file
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
        pos = 0
        files_path = os.path.dirname(os.path.abspath(__file__))
        self.folder_creation()
        self.react_project_creation()
        FILES_TO_COPY = ["babel.config.json","webpack.config.js"]
        print("5- Configuring react files ...")
      
        for files in FILES_TO_COPY:
           shutil.copy(os.path.join(files_path,"files",files),
                     os.path.join(self.path,self.name,"frontend"))

        shutil.copy(os.path.join(files_path,"files","index.html"),
                    os.path.join(self.path,self.name,"frontend","templates","frontend"))  
        shutil.copy(os.path.join(files_path,"files","urls.py.fe"),
                    os.path.join(self.path,self.name,"frontend","urls.py"))  
        
        shutil.copy(os.path.join(files_path,"files","Apps.js"),
                    os.path.join(self.path,self.name,"frontend","src","components"))    

        packagejs_path = os.path.join(self.path,self.name,"frontend","package.json")       
    
        data = read_file(packagejs_path)
    
        for dt in data:
            if '"test"' in dt:
                location = data.index(dt)  
        data[location] = '\t\t"dev": "webpack --mode development --watch",\n'    
        data.insert(location+1,'\t\t"build": "webpack --mode production"\n')   
        write_file(packagejs_path,data)
        write_file(os.path.join(self.path,self.name,"frontend","src","index.js"),
                    ['import App from "./components/Apps";\n'])
       
        ## Django Files
        views_path = os.path.join(self.path,self.name,"frontend","views.py")
        data = ["from django.shortcuts import render\n","def index(request, *args,**kwargs):","\treturn render(request,'frontend/index.html')"]
        write_file(views_path,data)  
        url_path = os.path.join(self.path,self.name,self.name,"urls.py")
        data = read_file(url_path)
        for dt in data:    
            if "urlpatterns" in dt:
                pos = data.index(dt)
        data.insert(pos+1,"path('', include('frontend.urls')),\n")  
        write_file(url_path,data)      
        settings_path= os.path.join(self.path,self.name,self.name,"settings.py")
        data = read_file(settings_path)
        for dt in data:
             if "INSTALLED_APPS" in dt:
                pos = data.index(dt)
        data.insert(pos+1,"\t'frontend.apps.FrontendConfig',\n") 
        write_file(settings_path,data)       
        # Run the react
        frontend_path= os.path.join(self.path,self.name,"frontend")
        backend_path = os.path.join(self.path,self.name)
        print("The configuration was done")  
        print("*"*self.size) 
        print("The integration was complete, you can start the application running the following commands:")
        print(f"FrontEnd: run the folowing command on {frontend_path}")
        print("   npm run dev")
        print(f"Backend: run the folowing command on {backend_path}")
        print("  python manage.py runserver")
        print("*"*self.size) 
           
          
        
     


