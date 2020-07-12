def memify(text):
    new = ''
    for i in range(len(text)):
        if i % 2:
            new += text[i].upper()
        else:
            new += text[i].lower()
    return new

print(memify('Believe all women'))
