import math
def int_fract(dec_num):
    int_part = "" #целая часть
    fract_part = "" #дробная часть
    flag = False
    for i in dec_num:
        if i ==",":
            flag = True
            continue
        if flag == False:
            int_part = int_part + i
        else:
            fract_part = fract_part + i
    return str(int_conv(int_part)) + "," + str(fract_conv(fract_part))

def int_conv(int_part):
    lenOfint_part = len(int_part)
    sum = 0
    power = 0
    cor = 1
    result = 0
    while power < lenOfint_part:
        number = int(int_part[power])
        sum = number * (2**(lenOfint_part - cor))
        power +=1
        cor +=1
        result = result + sum
    return result

def fract_conv(fract_part):
    lenOffract_part = len(fract_part)
    sum = 0
    power = 0
    cor = -1
    result = 0
    while power < lenOffract_part:
        number = int(fract_part[power])
        # print(number)
        sum = number * (2**(cor))
        # print(sum)
        power +=1
        cor -=1
        result = result + sum
    result = str(result)
    return result[2:]

if __name__ == "__main__":
    dec_num = str(input("введите целое число: "))
    print(int_fract(dec_num))