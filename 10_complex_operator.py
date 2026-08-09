#Predict outputs of complex operator expressions.
a = 10
b = 3
c = 0

print("1.", a + b * 2)#16
print("2.", (a + b) * 2)#26
print("3.", a / b)#3
print("4.", a // b)#3
print("5.", a % b)#1
print("6.", a ** 2)#100

print("7.", a > b)#True
print("8.", a < b)#False
print("9.", a == b)#False
print("10.", a != b)#True

print("11.", a > b and b > c)#False
print("12.", a < b or b > c)#True
print("13.", not(a > b))#False

print("14.", a and b)#3
print("15.", c and b)#0
print("16.", a or c)#10
print("17.", c or b)#3

print("18.", a & b)
print("19.", a | b)
print("20.", a ^ b)
print("21.", a << 1)
print("22.", a >> 1)

print("23.", True + False)
print("24.", bool(""))
print("25.", bool("Python"))
print("26.", bool([]))
print("27.", bool([1, 2]))

print("28.", a > b == True)
print("29.", a + b > 10 and a - b < 10)
print("30.", (a + b) % 2 == 0)