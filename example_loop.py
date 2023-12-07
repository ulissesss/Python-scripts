value = 0
# this is an exclusive range from 0 to 6 with a stride of 1
for i in range(0, 6, 1):
    value += i

# this will print True
print(value == 15)

value = 0
# this is an exclusive range from 0 to 10 with a stride of 2
for i in range(0, 10, 2):
    value += i

# we only ever added even numbers this time
# so a division with 2 will have no remainder
print((value % 2) == 0)


value2 = 1
while value > 0:
    value2 *= 2
    value -= 2

# these will print True
print(value <= 0)
print(value2 == 1024)
