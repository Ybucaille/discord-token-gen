import random
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

for i in range(10000):
    first = ''.join((random.choice(chars) for i in range(24)))
    second = ''.join((random.choice(chars) for i in range(6)))
    third = ''.join((random.choice(chars) for i in range(2)))
    fourth = ''.join((random.choice(chars) for i in range(26)))
    fifth = ''.join((random.choice(chars) for i in range(7)))
    result = first + "." + second + "." + third + "__" + fourth + "_" + fifth
    output = open("tokens.txt", "a")
    output.write(result + "\n")

