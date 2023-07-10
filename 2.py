str1 = str(input("Enter the first string:\n"))
str2 = str(input("Enter the second string:\n"))
str3 = ''
temp = 0
len1 = len(str1)
len2 = len(str2)

for iter1 in range(0, len2):
    for iter2 in range(temp, len1):
        if str2[iter1] == str1[iter2]:
            str3 += str1[iter2]
            temp = iter2 + 1
            break

if str2 == str3:
    print("yes")
else:
    print("no")
