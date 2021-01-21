def read_file(path):
	with open(path,"r") as file:
		data = file.readlines()
	return data	
def write_file(path,data):
	with open(path,"w")	as file:
		file.writelines(data)

