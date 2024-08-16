text=input("Enter text: ")
for i in range(len(text)):
    if text[i].upper():
        new_text="Yes"
    else:
        new_text="No"
print(new_text)