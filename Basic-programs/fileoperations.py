
#f=open("aaa.txt","r")
#text=f.read()
#print(text)



f=open("aaa.txt","w")
f.write("hello world")
f.close()
f=open("aaa.txt","r")
text=f.read()
print(text)