# author : YANG CUI
"""
Given a collection of numbers that might contain duplicates,
return all possible unique permutations.
"""

def listDeepCopy(inputList):
    copy = [0] * len(inputList)
    for i in range(len(inputList)):
        copy[i] = inputList[i]
    return copy

def permute_aux(inputList):
    inputList.sort()
    digitLeft = inputList
    listOfPermutes = []
    result = []
    return permute(digitLeft, result, listOfPermutes)

def permute(digitLeft, result, listOfPermutes):
    # base case:
    if digitLeft == []:
        if result not in listOfPermutes:
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


print(permute_aux([3,1,-1,0,1]))
