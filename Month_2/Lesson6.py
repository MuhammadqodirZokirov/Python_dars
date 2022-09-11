# def bolish(a, b):
#     result = 0
#     while a >= b:
#         a = a - b
#         result += 1
#     print(result, ".", a)
#
#
# bolish(55, 5)
# def PowerA3(a, b, c, d, e):
#     qiymatlar = [a, b, c, d, e]
#     for result in qiymatlar:
#         t = result ** 3
#         print(t)
#
# PowerA3(5, 8, 9, 6, 12)


# def MEAN(a, b, c, d):
#     print((a + b) / 2)
#     print(sqrt(a * b))
#     print((a + c) / 2)
#     print(sqrt(a * c))
#     print((a + d) / 2)
#     print(sqrt(a * d))
#
#
# MEAN(15, 56, 25, 989)

Abrorbek = {'soz': 300,
            "vaqt": 5,
            "xatolar": 7
            }
Fayzullo = {
    'soz': 220,
    "vaqt": 4,
    "xatolar": 2
}

tezlikA = Abrorbek["soz"] / Abrorbek["vaqt"]
sifatA = Abrorbek["xatolar"] / Abrorbek["soz"]
sifattezlikA = tezlikA * sifatA
tezlikF = Fayzullo["soz"] / Fayzullo["vaqt"]
sifatF = Fayzullo["xatolar"] / Fayzullo["soz"]
sifattezlikF = tezlikF * sifatF

print(sifattezlikA, sifattezlikF)
