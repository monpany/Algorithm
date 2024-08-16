text = "3 4 5 6"
result=""
for i in range(len(text)):
    if text[i]!=" ":
        result+=text[i]
print(result)
# ______
text="3 4 5 6"
result=""
for char in text:
    if char!=" ":
        result+=str(int(char)*2)
print(result)