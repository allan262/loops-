t=int(input("Enter the no. of terms: "))
a,b=0,1
print(a,end='')
print(b,end='')
for t in range(0,t-2):
    c=a+b
    print(c,end='')
    a=b
    b=c
