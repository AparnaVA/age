'''row=5
for i in range(0,row):
    for j in range(i+1):
        print(j+1 ,end="")
    print()
    '''
"""   
row=5
for i in range(row):
    for j in range(row):
        if j<=i:
            print(" ",end=" ")
        else:
            print("*" ,end=" ")
    print()
    """