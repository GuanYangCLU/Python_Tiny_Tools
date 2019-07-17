# test zip
str1 = 'abcd'
str2 = 'abdcf'
str3 = 'abceee'
print(zip(str1, str2))
print(list(zip(str1,str2,str3)))

# test lambda
print(list(filter(lambda x: True if x % 3 == 0 else False, range(100))))
print(list(map(lambda x: True if x % 3 == 0 else False, range(100))))

def mtp(n):
    return lambda x: x * n

three = mtp(3)
print(three(5))

# test input
factor = 2
a = input('Please input your number: ')
print(factor * int(a))

# test filter
a = [1,2,3,4,5,6]    
list = [i for i in filter(lambda a: a%2 == 1, a)]
print(list)
