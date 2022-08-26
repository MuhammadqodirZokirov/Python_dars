# txt = 'hello world 11569568956296'
# for c in txt:
#     print(c)

# for fruit in ["Apple", "Banana", "Peach", "Orange", "Durian", "Papaya"]:
#     print(fruit)


# for i in range(3, 7):
#     print(i)
# txt = 'hello world'
# for c in txt:
#     if c == ' ':
#         break
#     print(c)

# for i in range(1, 1000):
#     if i == 596:
#         break
#     print(i)

# txt = 'hello wo rld'
# for c in txt:
#     if c == 'o':
#         continue
#     print(c)
# for i in range(1, 10):
#     if i == 4:
#         continue
#     print(i)


# mevalar = ["Apple", "Banana", "Peach", "Orange", "Durian", "Papaya"]
# for i in mevalar:
#     if i =="Kakao" or i == "Orange":
#         break
#     print(i)
# mevalar = ["Apple", "Banana", "Peach", "Orange", "Durian", "Papaya"]
# for i in mevalar:
#     if i =="Durian" or i == "Orange":
#         continue
#     print(i)

# txt = 'hello world'
# for cr in txt:
#     if cr == ' ':
#         continue
#     if cr == 'r':
#         break
#     print(cr)
# print('DONE')
# from Lesson1 import a
# print(a)

# son = 1000
# for i in range(0, 1000):
#     son %= 3
#     print(son)

# 6-masala
# son = 1.0
# konfet_narxi = 10000
# for i in range(0, 5):
#     son += 0.2
#     print(f"{son} kg konfet narxi {son*konfet_narxi} so'm")

# # 7-masala
#
# count = 0
# a = int(input("a = "))
# b = int(input("b = "))
# for i in range(a, b+1):
#     count += i
# print(count)


# 8-masala
#
# count = 0
# a = int(input("a = "))
# b = int(input("b = "))
# for i in range(a, b+1):
#     count *= i
# print(count)


# 9-masala
#
# count = 0
# a = int(input("a = "))
# b = int(input("b = "))
# for i in range(a, b+1):
#     count += i**2
# print(count)


# 10 - masala
s = 1
n = int(input("n = "))

for i in range(1, n + 1):
    s += 1 / i
    print(f"{s}+ {1/i} = {s+ 1/i}")
print(s)
