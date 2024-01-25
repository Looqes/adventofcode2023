inputdata = [x.strip() for x in open("input1.txt").readlines()]

# print(inputdata)

wordnumbers = dict({
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
})

result = 0

for line in inputdata:
    numbersinline = []

    for i, character in enumerate(line):
        if character.isdigit():
            numbersinline.append(character)
        else:
            for wordnumber in wordnumbers:
                if line[i:].startswith(wordnumber):
                    numbersinline.append(wordnumbers[wordnumber])
    result += int(numbersinline[0] + numbersinline[-1])

print(result)








            

