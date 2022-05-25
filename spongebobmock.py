text = str(input("text: "))
text = text.lower()
formattedtext = ""
for i in range(len(text)):
    if i % 2 == 1:
        formattedtext = formattedtext + text[i].capitalize()
    else:
        formattedtext = formattedtext + text[i]
print(formattedtext)