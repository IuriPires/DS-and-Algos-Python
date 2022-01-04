# Binary search has a log N (Big (O))

def binary_search(list, number):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        attempt = list[mid]

        if attempt == number:
            return mid
        if attempt > number:
            high = mid - 1
        else:
            low = mid + 1
    return None

list = [1,3,5,7,9,11,12,14]

print(binary_search(list, 11))
print(list[5])