def raise_power(base_num,powe_num):
    result = 1
    for index in range(powe_num):
        result = result * base_num
    return result
print(raise_power(3,4))  