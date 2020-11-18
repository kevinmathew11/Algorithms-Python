def case_insensitive_comparison(s1,s2):
    return s1.upper() == s2.upper()


#Time and Space Complexity: Linear Memory

## Methods to optimize : Compare lengths at first: 

s1='avcc'
s1_iter=iter(s1)
print(s1_iter)