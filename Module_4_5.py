def get_multiplied_digits(number):
    str_number = str(number)

    if len(str_number) > 1:
        first = int(str_number[0])
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return int(str_number)

result = get_multiplied_digits(40203)
print(result)

result2 = get_multiplied_digits(30942) # Почему если последняя цифра в числе будет =0, то ответ тоже =0, а не 216?
print(result2)