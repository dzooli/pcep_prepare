
# textfile is an iterable class
with open('textfile.txt', "r") as input_file:
    for line in input_file:
        print(line.strip())