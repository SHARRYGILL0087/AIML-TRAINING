a = []
a.append(23)
a.append("Sg")
b = [23,"AJ",[69,"AC"]]
a.extend(b)
# print(a)
c = [2,"bjc",[8,9,"bc"]]
# a =  [23, 'Sg', 23, 'AJ', [69, 'AC'], 2, 'bjc', [8, 9, 'bc'], [2,"bjc",[8,9,"bc"]]
a.extend(c)
# a =  [23, 'Sg', 23, 'AJ', [69, 'AC'], 2, 'bjc', [8, 9, 'bc']]
a.pop(1)
a.remove([8, 9, 'bc'])
print(a)
a.clear()
print(a)
del a
a = 23 # int
b = 53.23 # float


