text = input("Introduce una cadena de text en minúsculas, sin tildes: ")
text = text.replace(" ", "")
text = text.lower()
if text == text[::-1]:
    print("SI")
else:
    print("NO")
