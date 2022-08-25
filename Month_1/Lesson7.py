# meva = ["olma", "behi", "shaftoli", "olcha", "banan"]
# meva.append("Anor")
# print(meva)
# thislist = ["apple", "banana", "cherry"]
# thislist.insert(2, "orange")
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# print(thislist)
# tropical = ["mango", "pineapple", "papaya"]
# print(tropical )
# thislist.extend(tropical)
# print(thislist)
# a_sinf = ["anvar","begzod","g'ani"]
# b_sinf = ["diyor","nodir","ali"]
# d_sinf = ["abbos","guli","lola"]
# print("                Maktab 44")
# print("Maktabimizga hush kelibsiz")
# sinf =input("Bizda A B D sinflar mavjud "
#             "qaybiriga qo'shilmoqchisiz\nSinfni kiriting>>")
# ism = input("Ismingizni kirirting>>>")
#
# if sinf.lower() == "a":
#     a_sinf.append(ism.title())
#     print(a_sinf)
# elif sinf.lower() == "b":
#     a_sinf.append(ism.title())
#     print(b_sinf)
# elif sinf.lower() == "d":
#     d_sinf.append(ism.title())
#     print(d_sinf)
# else:
#     print("Bizda bunday sinif mavjud emas!!!")
# umumiy = []
# umumiy.extend(a_sinf)
# umumiy.extend(b_sinf)
# umumiy.extend(d_sinf)
# print(umumiy)
#123
#231

# a = int(input("Uchxonali son kiriting>>> "))
# yuzlar = a // 100
# print(f"Yuzlar{yuzlar}")
# ikki = a % 100
# onlar = ikki//10
# print(f"Onlar {onlar}")
# birlar = ikki % 10
# print(f"Birlar {birlar}")
# print(onlar*100+birlar*10 +yuzlar)
# a = int(input("Uchxonali son kiriting>>> "))
# yuzlar = a // 100
# print(f"Yuzlar{yuzlar}")
# ikki = a % 100
# onlar = ikki//10
# print(f"Onlar {onlar}")
# birlar = ikki % 10
# print(f"Birlar {birlar}")
# print(birlar*100+yuzlar*10 +onlar)

# 123
# 312

# a = int(input("Uchxonali son kiriting>>> "))
# yuzlar = a // 100
# print(f"Yuzlar{yuzlar}")
# ikki = a % 100
# onlar = ikki//10
# print(f"Onlar {onlar}")
# birlar = ikki % 10
# print(f"Birlar {birlar}")
# print(onlar*100+yuzlar*10 +birlar)


# 1 2 3 2*100 = 200 +1*10 =210+3 = 213


a= int(input("To'rt xonali son kiriting>>> "))
yuzlik = a % 1000
print(yuzlik)
b = yuzlik//100
print(b)