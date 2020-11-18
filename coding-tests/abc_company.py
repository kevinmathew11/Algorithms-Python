
import random 
nums=[]
for i in range(10):
    nums.append(i)

#Shuffling the items in the list     
random.shuffle(nums)

nums_list=nums[:5]

#In python3, the dictionary is ordered by default.

ordered_dict={}

for index,key in enumerate(nums_list):           # Enumerating the list to create key,value pairs for the dictionary defined above
    if index==0:                             
        ordered_dict[key]=nums_list[-1] * 2      # For first item, the value would be twice the last item in the list.
    else:
        ordered_dict[key]=nums_list[index-1]*2   # Value of all other item in the list would be twice the previous value.
print(ordered_dict)




