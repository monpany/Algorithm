text="3 4 5 6"
result=""
for char in range(len(text)):
    if text[char]!=" ":
        result+=text[char]
print(result)

_______Q2

text="3456"
number=0
for i in range(len(text)):
    number+=int(text[i])
print(number)