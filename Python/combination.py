i=1
counter=0
while i<=7:
    j=i+1
    while j<=7:
        k=j+1
        while k<=7:
            l=k+1
            while l<=7:
                print("%d%d%d%d" % (i,j,k,l))
                counter=counter+1
                l=l+1
            k=k+1
        j=j+1
    i=i+1
print("counter is %d" % counter)