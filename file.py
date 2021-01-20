import os
no = __file__.replace(os.path.basename(__file__),"")  
print('__file__:    ', __file__)
print(os.path.join(os.path.dirname(os.path.abspath(__file__)),"files"))