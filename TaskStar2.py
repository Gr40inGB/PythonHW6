# n = '16856833'
# n = '14016856833'
# n = '9996'
n = '234523642345789812354678654323454919865'


# n = input("Please input number: ")

def print_all(number, sign):
    if len(number) > 3:
        return sign * int(number[-3:]) + print_all(number[:-3], -1 if sign == 1 else 1)
    else:
        return sign * int(number)


print(f'Number {n.strip()} is{" not" if print_all(n.strip(), +1) % 7 else ""} divisible for seven')
