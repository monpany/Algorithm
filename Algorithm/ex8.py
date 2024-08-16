number=0
text = "9394884039"
for char in text:
    if char=="8":
        number+=1
print(number)
# ________
text = "93948554039"
isfound = False
index = 0
while index < len(text) and not isfound:
    if text[index] == "8":
        result = index
        isfound = True
    index += 1

if isfound:
    print(result)
else:
    print("No number 8")
_________

text = "98394554039"
result = "No number 8"
index = 0
while index < len(text):
    if text[index] == "8":
        result = index
        index = len(text)
    index += 1
print(result)