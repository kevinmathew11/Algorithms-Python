#2. Loop and Join
inp='foo bar'
reversedString=[]
indx=len(inp) 
while indx>0 :
    reversedString += inp[indx-1]
    indx=indx-1

a='-'
r1=a.join(reversedString)

print(reversedString)
print("r1=",r1)

#print(r)

tup=('1','2','c')
print(type(reversedString))
print(type(tup))
tup1='.'.join(tup)
r1=''.join(reversedString)

print(tup1)