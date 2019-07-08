# a = 1
# while a < 10:
#     b = 0
#     while b < a:
#         print("*", end = '')
#         b = b + 1
#     print()
#     a = a + 1

# a = 10
# while a > 1:
#     b = 0
#     while b < a:
#         print("*", end = '')
#         b = b + 1
#     print()
#     a = a - 1

# 10 is the total number to print
for num in range(10):
    for i in range(num):
        print ("*", end="")
    print()

# for num in range(10, 0, -1):
#     print(num)

for num in range(10, 1, -1):
    for i in range(num):
        print ("*", end="")
    print()