testarray = [4,-2,3,-7,5,2,-6,8,-4,3,-2,1]

def maxSum(arr):
    sumarray = []
    for i in arr:
        sumarray.append(sum(i))
    maxsum = max(sumarray)
    return (maxsum, sumarray.index(maxsum))


def bruteforce_max(arr):
    allarray = []
    sizeofarray = len(arr)

    for i in range(sizeofarray):

        for j in range(1, sizeofarray + 1):

            if i + j <= sizeofarray:
                allarray.append(arr[i:i + j])

    maxsublistindex = maxSum(allarray)[1]
    maxsum = maxSum(allarray)[0]

    return ('Max Subarray = ' + str(allarray[maxsublistindex]),
            'Max Sum = ' + str(maxsum))



print(bruteforce_max(testarray))



        


