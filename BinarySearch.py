#Elements should already be sorted
#Essentially split the list in half. If greater move right, if less move left
#Recall the function on the left or right half as needed
#return the middle element if it matches what we are looking for

#Code found on geeksforgeeks.org

#Recursive binary search
#time complexity:  O(log n)
#space complexity: O(log n) <-recusion creates Call Stack 
def binary_search(arr, low, high, x):
    #check base case
    if high >= low:
        mid = (high + low) // 2

        #return middle if that is what were looking for
        if arr[mid] == x:
            return mid
        
        #change low/high to be 1 +/- the midpoint based on dir
        #smaller than mid, must be in left side
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        
        #else its to the right
        else:
            return binary_search(arr, mid + 1, high, x)
        
    else:
        #Element not present so return err code
        return -1
    
#Iterateive binary search
def binary_search_it(arr, x):
    low = 0
    high = len(arr) -1
    mid = 0
    
    #iterate through until we hit mid
    while low < high:
        mid = (high + low) // 2

        #If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1

        #If x is smaller, ignore right
        elif arr[mid] > x:
            high = mid - 1
        
        else:
            return mid
        
    #element was not in list, return err code
    return - 1


arr = [ 2, 3, 5, 10, 40]
x = 10

#test func
result1 = binary_search(arr, 0, len(arr)-1, x)
result2 = binary_search_it(arr, x)

if result1 != -1:
    print("Element is present at index", str(result1), ", found by recusion")
else:
    print("Element is not present in array via recusion")

if result2 != -1:
    print("Element is present at index", str(result2), ", found by iterative process")
else:
    print("Element is not present in array via iterative process")