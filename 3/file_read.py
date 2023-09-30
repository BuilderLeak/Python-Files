#file2 = open(a,'r')
file = open('abc.txt','r')
line = file.readline()
while(line!=""):
  print(line)
  line = file.readline()
file.close()