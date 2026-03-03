lst = list(map(int, input("Enter numbers separated by space: ").split()))

unique_list = list(set(lst))
print("After removing duplicates:", unique_list)