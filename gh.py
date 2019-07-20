X1=int(input())
if X1>1:
    for i in range(2,X1):
        if X1%i==0:
            print("no")
            break
    else:
        print("yes")
else:
    print("no")
