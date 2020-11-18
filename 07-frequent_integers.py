

sequence=[9,9,5,6,7,4,2,2]

from collections import Counter


a=Counter(sequence)
print(a)

#print(a.key[max(a.values())])

max_val=max(a.values())
key_list=list(a.keys())

print ([k for k,v in a.items() if v == max_val])