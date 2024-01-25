
puzzleinput = [line.strip("\n") for line in open("input1.txt").readlines()]



numberlists = [[char for char in line if char.isdigit()] for line in puzzleinput]


result = sum([int(numlist[0] + numlist[-1]) for numlist in numberlists])


print(result)