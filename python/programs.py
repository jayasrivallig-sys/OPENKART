# l = ["aeropale", "water is wated","bananana", "swetete", "is"]
# print(max(l))
# print(max(l, key=len))
# print(len(max(l,key=len)))

# print(min(l))
# print(min(l,key=len))
# print(len(min(l, key=len)))

# string =  input("String :" )
# v=0
# c=0
# string.lower()
# for i in string:
#     if i in "aeiou":
#         v = v+1
#     else:
#         c=c+1
# print(v,c)


# num = [2,3]
# sum = 0
# for i in num:
#     sum = sum + i**2
# print(sum)

# nuk = [1,2,3,4,5]
# sum1 =0
# for i in nuk:
#     sum1 = sum1+i
# print(sum1)

# a = "sapient India"
# m = a.replace('a', '@')
# f = []
# f.append(m)
# print(m)

numbers = [1, 2, 3, 2, 4, 2, 5, 3, 3, 3, 9, 9, 9, 9, 9, 9]
highest = max(set(numbers), key=numbers.count)

count_high = numbers.count(highest)

print(count_high)
print(highest)