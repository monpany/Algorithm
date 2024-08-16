num1 = int(input("Number 1: "))
max_value = num1
min_value = num1
for i in range(2, 6):
    num = int(input("Number " + str(i) + ": ")) 
    if num > max_value:
        max_value = num
    if num < min_value:
        min_value = num
print("Max: " , max_value)
print("Min: " , min_value)