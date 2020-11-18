"""
Given a value, return the optimal number of coins [1,5,10,25] to make the value.

Given a value and a set of coins, return the optimal count of coins to achieve the value 


33 cents: 1 quarter (25) , 1 nickel (5) 3 pennies(1) [ dime 10]

#num_coins(33) => 5 

"""



def greedy_num_coins(cents):


    if cents < 1:
        return 0     
    coins=[3,1,5,4]

    num_of_coins= 0
    #coins={'q':25,'n':5,'p':1,'d':10} 

    for coin in coins:
        num_of_coins+= cents // coin
        #print(num_of_coins)
        cents = cents % coin
        if cents == 0:
            break
    return num_of_coins    


def 


d1={}
d1=num_keys_dict
for i,(key,value) in enumerate(num_keys_dict.items()):
    if (i==0):
        continue
    d1.value= 2 * num_keys_dict[i-1]
    print(d1.value)
    

# Lets initialize the dictionary 

num_keys_dict=dict.fromkeys(num_keys)

print(num_keys_dict)

#for k,v in num_keys_dict.items():
#    print(k,v)




#Value corresponding to the key  should be value of prev

print("greedy:",greedy_num_coins(7))


