import sys

digit_string = sys.argv[1]

if digit_string.isdigit():
    digit_string = int(digit_string)
    space = " "
    lattice = "#"
    for i in range(digit_string + 1):
        if i == 0:
            continue
        print(space * (digit_string-i) + lattice *(digit_string - (digit_string -i)))
else:
    print("Вы ввели неправильные символы, нужно ввести только число > 0 в аргументе")