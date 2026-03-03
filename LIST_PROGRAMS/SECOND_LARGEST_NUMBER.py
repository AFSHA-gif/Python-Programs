lst = list(map(int, input("Enter numbers separated by space: ").split()))

lst = list(set(lst))  # remove duplicates
lst.sort()

print("Second largest:", lst[-2])