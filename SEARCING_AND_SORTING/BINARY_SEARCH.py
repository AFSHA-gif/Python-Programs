lst = list(map(int, input("Enter sorted numbers: ").split()))
key = int(input("Enter element to search: "))

low = 0
high = len(lst) - 1

while low <= high:
    mid = (low + high) // 2
    if lst[mid] == key:
        print("Element found at index", mid)
        break
    elif lst[mid] < key:
        low = mid + 1
    else:
        high = mid - 1
else:
    print("Element not found")