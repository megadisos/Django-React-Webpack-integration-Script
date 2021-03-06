import os
from shutil import copyfile
from react_app_creation import ReactAppCreation
from integration_files.aditional_tasks import read_file, write_file
class Api_creation():
    def __init__(self, name,path,size):
        self.name = name
        self.path = path
        self.size = size
    def api_creation(self):
        FILES_TO_DELETE = ["models.py","views.py","serializers.py","urls.py"]
        location = 0
        location2 = 0
        loc= 0
        print("2- Creating the API ...")
        # set the paths
        path = os.path.join(self.path,self.name)
        os.chdir(path)
        os.system("django-admin startapp api")
        os.chdir(os.path.join(path,"api"))
        # remove files
        np = __file__.replace(os.path.basename(__file__),"")  
        for fl in FILES_TO_DELETE:
            if os.path.exists(fl):
                os.remove(fl)  
        # copy the new files        
        for fl in FILES_TO_DELETE:
            if os.path.exists(os.path.join(np,"files",fl)):
                copyfile(os.path.join(np,"files",fl),os.path.join(os.getcwd(),fl)) 
        # Editing the settings.py file
        settings_path = os.path.join(self.path,self.name,self.name,"settings.py")
        print(settings_path)
        data = read_file(settings_path)
        for dt in data:
            if "INSTALLED_APPS" in dt:
                location = data.index(dt)
            elif "'DIRS': []," in dt:
                loc = data.index(dt)
                print(loc)

        data.insert(location+1,"\t'rest_framework',\n")
        data.insert(location+2,"\t'api',\n")       
        pt = os.path.join(self.path,self.name,"frontend","templates")
        data[loc+2] = "\t\t'DIRS': [r'"+pt+"'],\n"
        write_file(settings_path,data)
            
        # Editing the urls.py file 
        url_path =   os.path.join(self.path,self.name,self.name,"urls.py")  
        data = read_file(url_path)
        for dt in data:
            if "from django.urls import path" in dt:
                location = data.index(dt)
            if "path('admin/', admin.site.urls)," in dt:
                location2 = data.index(dt)

        data[location] = "from django.urls import path,include" 

        data.insert(location2+1,"\tpath('',include('api.urls')),\n")   
        write_file(url_path,data)
        # Makemigrations
        os.chdir(os.path.join(self.path,self.name))
        print(" 2.1- Runing Makemigrations ...")
        os.system("python manage.py makemigrations")
        print(" 2.2- Runing migrations ...")
        os.system("python manage.py migrate")
        print("")
        print(f"The API was created")
        print("*"*self.size)
        react = ReactAppCreation(self.size, self.path,self.name)
        react.files_configuration()

