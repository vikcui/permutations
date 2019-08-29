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
        listOfPermutes.append(listDeepCopy(result))
    # choose/explore/unchoos
    else:
        for i in range(len(digitLeft)):
            if i == 0:
                # choose
                digit = digitLeft[i]
                result.append(digit)
                digitLeft.remove(digitLeft[i])

                # explore
                permute(digitLeft, result,listOfPermutes )

                # un - choose
                digitLeft.insert(i, digit)
                result.__delitem__(len(result) - 1)
            else:
                # only go in if the element is unique
                if digitLeft[i] != digitLeft[i - 1]:
                    # choose
                    digit = digitLeft[i]
                    result.append(digit)
                    digitLeft.remove(digitLeft[i])

                    # explore
                    permute(digitLeft, result, listOfPermutes)

                    # un - choose
                    digitLeft.insert(i, digit)
                    result.__delitem__(len(result) - 1)
        return listOfPermutes

print(permute_aux([3,1,-1,0,1]))
