text = "454639"
even_count=0
for i in range(len(text)):
    if int(text[i])% 2  ==  1:
       even_count += int(text[i])
print("even_count",even_count)
_____Q2 #Sum all number
text = "454639"
even_count=0
for i in range(len(text)):
    if int(text[i])% 2  ==  1 or int(text[i])% 2 == 0:
       even_count += int(text[i])

print(even_count)
_____Q3 #Sum only even number 
text = "454639"
even_count=0
for i in range(len(text)):
    if int(text[i])% 2  ==  0:
       even_count += int(text[i])
print(even_count)
_____Q4 #Reverse 
text="454639"
print(text[::-1])