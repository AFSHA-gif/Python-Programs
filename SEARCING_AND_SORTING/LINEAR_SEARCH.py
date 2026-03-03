st = list(map(int, input("Enter numbers: ").split()))
key = int(input("Enter element to search: "))

for i in range(len(list)):
    if list[i] == key:
        print("Element found at index", i)
        break
else:
    print("Element not found")