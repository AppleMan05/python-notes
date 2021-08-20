#if statements

is_male = True

if is_male:
    print("you are a male")
else:
    print("you are not a male")

is_tall = True

if is_male or is_tall:
    print("youre either tall or male or both")
else:
    print("youre neither male nor tall")

if is_male and is_tall:
    print("youre tall and male")
elif is_male and not(is_tall):
    print("youre male and short")
elif not(is_male) and is_tall:
    print("youre not male but tall")
else: 
    print("youre either not male or not tall or both")


def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(3, 4, 5))

