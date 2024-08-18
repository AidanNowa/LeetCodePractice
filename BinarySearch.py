#Elements should already be sorted
#Essentially split the list in half. If greater move right, if less move left
#Recall the function on the left or right half as needed
#return the middle element if it matches what we are looking for

#Code found on geeksforgeeks.org

#Recursive binary search
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
    
arr = [ 2, 3, 5, 10, 40]
x = 10

#test func
result = binary_search(arr, 0, len(arr)-1, x)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")