def binary_search(values, key):
    l = 0
    r = len(values)-1
    while(l <= r):
        mid = (l + r) // 2
        if values[mid] == key:
            return True
        elif values[mid] < key:
            l = mid + 1
        else :
            r = mid - 1

    return False