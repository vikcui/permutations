# author: YANG CUI
"""
Given a collection of distinct integers,
return all possible permutations.
"""

"""
function permute(num)
    pesudocode of backtracking 
    
    if empty: nothing to do 
    else:
        for each digit in num:
        choose that digit to be first 
        permute(the rest of num)
        un-choose that digit

"""
def listDeepCopy(inputList):
    copy = [0] * len(inputList)
    for i in range(len(inputList)):
        copy[i] = inputList[i]
    return copy

def permute_aux(inputList):
    digitLeft = inputList
    listOfPermutes = []
    result = []
    return permute(digitLeft, result, listOfPermutes)

def permute(digitLeft, result, listOfPermutes):
    # base case:
    if digitLeft == []:
        listOfPermutes.append(listDeepCopy(result))
    # choose/explore/unchoos
    else:
        for i in range(len(digitLeft)):
            # choose
            digit = digitLeft[i]
            result.append(digit)
            digitLeft.remove(digitLeft[i])

            # explore
            permute(digitLeft, result,listOfPermutes )

            # un - choose
            digitLeft.insert(i, digit)
            result.__delitem__(len(result) - 1)
    return listOfPermutes


# print(permute_aux([1, 2, 3]))


