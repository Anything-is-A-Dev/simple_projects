import random


letter = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
          "w", "x", "y", "z"]
num = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

special = ["!", "@", "#", "$", "%", "^", "*", "-", "_", "=", "+", "/", "?"]

Password = ""

l = random.choice(letter)
l2 = random.choice(letter)
l3 = random.choice(letter)
l4 = random.choice(letter)
l5 = random.choice(letter)

n = random.choice(num)
n2 = random.choice(num)
n3 = random.choice(num)

s = random.choice(special)
s1 = random.choice(special)
s2 = random.choice(special)

Password = l + n + l3 + s + l2 + l + n2 + l5 + l4 + s2 + n3 + s1

print(Password)



