n = int(input())
i = 1
list1 = []
while i < n + 1:
    if i % 2 != 1:
        list1.append('I love that')
    else:
        list1.append('I hate that')
    i += 1

str1 = ' '.join(list1)
str1 = str1[::-1]
str1 = str1.replace('taht', 'ti', 1)
str1 = str1[::-1]
print(str1)
