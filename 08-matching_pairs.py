'''

https://www.youtube.com/watch?v=wBXZD436JAg


x

def find_pairs(sequence,target): # list and target number
    '''
    Hint: Traverse through the list once, What possible information can we get about each element while traversing?

    COMPLEMENT for each number to reach the target sum.
    
        INPUT                   [1,2,3,4,5,6,9,11] and target is 9
    list of complements will be [8,7,6,5,4,3,0,-2]

    '''
    complements=set()
    print("c",complements)
    for element in sequence:
        if element in complements:
            print(element,target-element)
            continue
        complements.add(target-element)
    return False

sequence=[1,2,3,4,6]
target=5

found=find_pairs(sequence,target)

print(found)

