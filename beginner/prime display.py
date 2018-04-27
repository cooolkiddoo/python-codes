a=int(input("Enter upper limit: "))
for r in range(2,r+1):
    k=0
    for i in range(2,r//2+1):
        if(r%i==0):
            k=k+1
    if(k<=0):
        print(r)
