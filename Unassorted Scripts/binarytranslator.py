data = [0b01101001,
        0b00011001,
        0b01101101,
        0b00100000,
        0b01101000,
        0b01110101,
        0b01101110,
        0b01100111,
        0b01110010,
        0b01111001] 

character = [chr(i) for i in data]
character[1] = "'"
joiner = "".join(character)
print(joiner)

new_data = []
for i in joiner:
    new_data.append(bin(ord(i)))

print(new_data)
