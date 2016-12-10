
#Binary search with strings
#Binary search requires a sorted list
MyList = ['ed','will','kasia','ilan']
MyList.sort()

def binary_search(array, target):
    lower = 0
    upper = len(array)
    while lower < upper:
        x = lower + (upper - lower) // 2
        val = array[x]
        if target == val:
            return x
        elif target > val:
            if lower == x:   # this two are the actual lines
                break        # you're looking for
            lower = x
        elif target < val:
            upper = x

print(binary_search(MyList,'ilan'))