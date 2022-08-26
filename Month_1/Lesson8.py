# Usul remove()belgilangan elementni olib tashlaydi.
# thislist = ["apple", "banana", "cherry"]
# print(thislist)
# thislist.remove("banana")
# print(thislist)
# Usul pop()belgilangan indeksni olib tashlaydi.
# thislist = ["apple", "banana", "cherry"]
# thislist.pop(2)
# print(thislist)
# Agar siz indeksni ko'rsatmasangiz, pop()usul oxirgi elementni olib tashlaydi.
# thislist = ["apple", "banana", "cherry"]
# thislist.pop()
# print(thislist)
# delKalit so'z belgilangan indeksni ham olib tashlaydi :
# thislist = ["apple", "banana", "cherry"]
# del thislist[0]
# print(thislist)
# delKalit so'z ham ro'yxatni butunlay o'chirib tashlashi mumkin .
# thislist = ["apple", "banana", "cherry"]
# del thislist


# Usul clear()ro'yxatni bo'shatadi.
#
# Ro'yxat hali ham saqlanib qolmoqda, ammo uning mazmuni yo'q.

# thislist = ["apple", "banana", "cherry"]
# thislist.clear()
# print(thislist)
#
# Roʻyxatni alfanumerik tartibda tartiblash
# Ro'yxat ob'ektlarida sort()ro'yxatni sukut bo'yicha alfanumerik, o'sish bo'yicha tartiblash usuli mavjud"
# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort()
# print(thislist)


# thislist = [10,1,15,5,29,6,6,5598,3,95,256,5,9,2,231,65]
# thislist.sort()
# print(thislist)

# thislist = ["orange", "mango", "kiwi", "pineapple", "banana",1,565,954,89,89,77,7,10,2,3,4,9]
# thislist.sort()
# print(thislist)

# Kamayish bo'yicha saralash
# Kamaytirish bo'yicha tartiblash uchun argument kalit so'zidan foydalaning reverse = True:
#
# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort(reverse = True)
# print(thislist)

# thislist = [100, 50, 65, 82, 23]
# thislist.sort(reverse = True)
# print(thislist)
# copy()Usul bilan ro'yxatning nusxasini yarating :
# thislist = ["apple", "banana", "cherry"]
# mylist = thislist.copy()
# print("mylist=",mylist)
# print("thislist=",thislist)
# thislist = ["apple", "banana", "cherry"]
# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]
#
# list3 = list1 + list2+thislist
# print(list3)

# fruits = ['apple', 'banana', 'cherry']
#
# x = fruits.index("cherry")
# print(x)

# fruits = ['banana','apple',  'cherry']
# print(fruits)
# fruits.reverse()
#
# print(fruits)

# fruits = ['apple', 'banana', 'cherry', 'cherry', 'cherry', 'cherry', 'cherry', 'cherry']
#
# x = fruits.count("cherry")
# print(x)

# a = 6
# b = 3
# print((a%2==1 and b%2==1 )or (a%2==0 and b%2==0) )


# otning yurishi 40-masala
# x = 1
# y = 2
# x1 = 3
# y1 = 3
#
# print(abs(y1 - y) == 2 and abs(x1 - x)==1 or abs(y1 - y) == 1 and abs(x1 - x) == 2)


# farzinning yurishi 39 - masala
# x = 3
# y = 1
# x1 = 6
# y1 = 4
# print(abs(x - y) ==abs(x1 - y1) or x==x1 or y==y1)


# filning yurishi 38-masala
# x = 3
# y = 1
# x1 = 6
# y1 = 4
#
# print(abs(x - y)==abs(x1 - y1))


# shohning yurishi 37-masala


x = 4
y = 1
x1 = 3
y1 = 1

print((x + y) % 2 == 1 and (x1 + y1) % 2 == 1 or (x + y) % 2 == 0 and (x1 + y1) % 2 == 0)
