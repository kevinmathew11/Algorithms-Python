
inp ="foo bar"

print(inp)


#1. Slicing 
# stringname[stringLength::-1]

print(inp[::-1])


#2. Loop and Join

reversedString=[]
indx=len(inp) 
while indx>0 :
    reversedString += inp[indx-1]
    indx=indx-1
    
#r1=''.join(reversedString)
print(r1)


# 3. reversed built in function and join

reversed=''.join(reversed(inp))
print(reversed)

# 4 . Recursion

def reverse(s): 
    """ 
    Here, string is passed as an argument to a recursive function to reverse the string. 
    In the function, the base condition is that if the length of the string is equal to 0, the string is returned. 
    If not equal to 0, the reverse function is recursively called to slice the part of the string except the first character 
    and concatenate the first character to the end of the sliced string.
    """
    if len(s) == 0: 
        return s 
    else: 
        return reverse(s[1:]) + s[0] 

print("recursion: ",reverse(inp))


# 5. one more loop

def loop2(s): 
  stri = "" 
  for i in s: 
    stri = i + stri
    print(i,stri)
  return stri 


print("s",loop2(inp))

