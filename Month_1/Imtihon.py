from random import randint

Abror = []
a = ['1',   '4', '5',   '9',    '14',  '18',   '21', '22', '24', '25',  '37', '40']
for i in range(5):
    m = randint(1, 12)
    Abror.append(a[m])
print(Abror)
