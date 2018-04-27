def floorSearch(arr, n, x):
 

    if (x >= arr[n - 1]):
        return n - 1

    if (x < arr[0]):
        return -1

 
    for i in range(1, n):
        if (arr[i] > x):
            return (i - 1)
 
    return -1

arr = [1, 2, 4, 6, 10, 12, 14]
n = len(arr)
x = 7
index = floorSearch(arr, n-1, x)
 
if (index == -1):
    print("Floor of", x, "doesn't exist in array ",
                                        end = "")
else:
    print("Floor of", x, "is", arr[index])
