# Print out Letters from A to Z


from string import ascii_lowercase


letters={letter: str(index) for index, letter in enumerate(ascii_lowercase,start=1)}

for element in letters:
    print(element)
