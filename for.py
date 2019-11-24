#for loop
n=int(input('Enter no of lines:'))

# pattern 1
for i in range(0,n+1):
    print("*"*i)

# pattern 2
for i in range(n,0,-1):
    print("*" * i)

# pattern 3
for i in range (n, 0, -1):
    print((n-i) * ' ' + i * '*')

# pattern 4
for i in range(1,n+1):
    print(" "*(n-i),"* "*i)

# pattern 5
for i in range(0,n+1):
    print((n - i) * ' ' + i * '*')

# pattern 6
data="python"
l=len(data)+1
# print(l)
for i in range(0,l):
    print((l - i) * ' ' +  data[0:i])



