
N=[9,8,7,6,5,4,3,2,1]
for i in N:
    j=1
    while j<=i:
        print(f'{j}*{i}={j*i}',end=" ")
        j+=1
    print()