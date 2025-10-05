for i in range(1,6):
    for j in range(1,6):
        if i==1 or j==3 and i==2 or j==3 and i==3 or j==3 and i==4 or j==3 and i==5 or j==2 and i==6:
            print("\t*",end="")
        else:
            print("\n")