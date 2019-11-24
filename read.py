import os
import re
li = os.listdir("demo")
print(li)
for i in li:
    net = os.path.splitext(i)
    if(net[1]==".log"):
        f = open("demo" +i, "rb")
        data = f.read().decode()
        pattern = '\S+@\S+'
        matches = re.findall(pattern, data)
        print(matches)
        f.close()
