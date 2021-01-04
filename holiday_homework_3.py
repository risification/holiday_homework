n = int(input())
list1 = []
for m in range(n):
    j = input()
    list1.append(j)
i = 1
while i <= n:
    list2 = []
    if len(list1[i - 1]) > 2:
        list2.append(list1[i - 1][0])
        list2.append(list1[i - 1][-1])
        char_list = []
        string = list1[i - 1][1:-1]
        for c in string:
            char_list.append(c)
        list3 = []
        for z in char_list:
            if z not in list3:
                list3.append(z)
        list3.insert(0, list2[0])
        list3.append(list2[1])
        str1 = ''.join(list3)
        print(str1)
        print(list1)
    else:
        print(list1[i - 1])
    i += 1
'''while i <= n:
    list2 = []
    if len(list1[i - 1]) > 2:
        list2.append(list1[i - 1][0])
        list2.append(list1[i - 1][-1])
        char_list = []
        list3 = list1[i - 1][1:-1]
        list3 = [list3[i:i + 2] for i in range(0, len(list3), 2)]
        k = 0
        while k < len(list3):
            list3 = len(list3)*list3[1][0]
            k += 1
            print(list3)

    else:
        print(list1[i - 1])
    i += 1
'''