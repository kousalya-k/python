import os
os.chdir("test/multiple/levels")
d=os.listdir()
for i in d:
   if os.path.isfile(i) and  os.path.splitext(i)[1]==".log":
       print(i)

for i in list(filter(lambda i:i.endswith('.log'),os.listdir())):
    with open(i,'r') as fo:
        print(fo.read())


