'''
https://www.mathblog.dk/project-euler-31-combinations-english-currency-denominations/

Algorithm explanation

'''


#Brute Force
def countwaysBruteForce(n):
    total = 0
    for onepound in range(0,n+1,100):
        for fifty in range(0,n+1-onepound,50):
            for twenty in range(0,n+1-onepound-fifty,20):
                for ten in range(0,n+1-onepound-fifty-twenty,10):
                    for five in range(0,n+1-onepound-fifty-twenty-ten,5):
                        for two in range(0,n+1-onepound-fifty-twenty-ten-five,2):
                            for one in range(n+1-onepound-fifty-twenty-ten-five-two):
                                if onepound+fifty+twenty+ten+five+two+one == n:
                                    total += 1

    return total

#print (countwaysBruteForce(300))


# Dynamic Programming

def countwaysDynamic(money,coin_index):
    count=0
    if coin_index <= 0:
        return 1 
    m = money
    if memoiz_list[m][coin_index] > 0 : 
        return memoiz_list[m][coin_index]
    while money >= 0 :
        count += countwaysDynamic(money,coin_index-1)
        money -= coin_list[coin_index]
    memoiz_list[m][coin_index] = count
    print( f"Index:{coin_index}, memoiz_list{memoiz_list}" )
    return count

coin_list = [1,2,5]
memoiz_list = [[0,0,0] for i in range(201)]
#print(countwaysDynamic(10,2)) #Replace problem_31_dynamic_programming() with problem_31



print(memo)