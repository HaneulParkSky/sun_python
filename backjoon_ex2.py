
# https://wikidocs.net/7020
# 147번 문제

a = [1,2,3]

for x in a:
    print("3 x " + str(x), "=", 3 * x)

print("------")

# 148번 문제 

b = ["a","b","c","d"]

bcd = b[1:]

for x in bcd:
    print(x)

print("------")


# 151번 문제

c = [3, -20, -3, 44]

for x in c:
    if x <0:
        print(x)

print("------")

# 152번 문제

d = [3, 100, 23, 44]

for x in d:
    if x % 3 == 0:
        print(x)


print("------")

# 153번 문제

e = [13,21,12,14,30,18]

for x in e:
    if(x < 20) and (x % 3 == 0):
        print(x)


print("------")

# 154번 문제

f = ["I", "study", "python", "language", "!"]

for x in f:
    if len(x) >= 3:
        print(x)

print("------")


# 155번 문제

g = ["A", "b", "c", "D"]

for x in g:
    if x.isupper():         #isupper() 메서드는 대문자 여부를 판별
        print(x)

print("------")
        

# 156번 문제

for x in g:
    if x.isupper() == False:
        print(x)
        
print("------")


# 162번 문제

for x in range(2002, 2051, 4):
    print(x)

print("------")

# 163번 문제

for x in range(3,31,3):
    print(x)
    

print("------")

# 165번 문제

for x in range(10):
    print(x/10)

print("------")


# 166번 문제

for x in range(1,10):
    print("3 x ", x, "=", 3 * x)

print("------")


# 167번 문제

num = 3
for x in range(1,10,2):
    print(num, "x", x, "=", 3 * x)

print("------")

# 168번 문제

sum = 0
for x in range(1,11):
    sum += x

print("Sum :", sum)

print("------")

# 171번 문제

price_list = [32100, 32150, 32000, 32500]

for x in range(4):
    print(price_list[x])
    
print("------")


    

    
