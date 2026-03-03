n = int(input("How many elements: "))
lst = []

for i in range(n):
    lst.append(int(input()))

print("Largest element:", max(lst))