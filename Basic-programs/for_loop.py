for i in range(0, 10 , 1): #exit from loop
    if i==5:
        break
    print(i)
print("hello")


for i in range(0, 10 , 1):  # continue used to skip the current iteration.
    if i==5:
        continue
    print(i)

    

for i in range(0, 10 , 1):  # pass used to avoid the error.
    if i==5:
        pass
    print(i)