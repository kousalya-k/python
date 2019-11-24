import os
import re
print(os.chdir("C:\\Users\\sn263\\Python_Training\\Test"))
print(os.getcwd())
for file in os.listdir("C:\\Users\\sn263\\Python_Training\\Test"):
    if file.endswith('.log'):
        fo=open(file,'r')
        for line in fo:
            s=re.findall('[^@]+@[^@]+\.[^@]+', line)
            if(len(s)!=0):
                print(s)



   

