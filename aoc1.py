#part 1

sum = 0
with open('input_1.txt') as f:
    lines = f.readlines()
    for line in lines:
        first_num = 0
        second_num = 0
        for char in line:
            if char.isdigit():
                if first_num == 0:
                    first_num = int(char)
                    second_num = first_num
                else:
                    second_num = int(char)
        sum += first_num *10 + second_num


print("answer 1: ")
print(sum)


## Part 2


spelled_numbers = {"one" : 1, "two" : 2, "three" : 3, "four" : 4, "five" : 5, "six" : 6,
                   "seven" : 7, "eight" : 8, "nine" : 9}

sum = 0
with open('input_1.txt') as f:
    lines = f.readlines()
    for line in lines:
        first_num = 0
        second_num = 0

        for index, char in enumerate(line):
            if char.isdigit():
                if first_num == 0:
                    first_num = int(char)
                    second_num = first_num
                else:
                    second_num = int(char)
            else:
                for spelled_number, val in spelled_numbers.items():
                    if line.find(spelled_number, index) == index:
                        if first_num == 0:
                            first_num = spelled_numbers[spelled_number]
                            second_num = first_num
                        else:
                            second_num = spelled_numbers[spelled_number]
                            break
                
        sum += first_num *10 + second_num

print("answer 2: ")
print(sum)