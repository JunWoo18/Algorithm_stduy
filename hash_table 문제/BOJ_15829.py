M=1234567891
r=31
rst=0

L=int(input()) 
small =input()

for i in range(L):
    rst += (ord(small[i])-96) * (r ** i)
print(rst % M)
