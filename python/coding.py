#rev string - palindrome
#count char
#remove deplicates
#anamgram
#even/odd
#div by a num
#prime, replace a char,try expect block, fibnocci, sum all of digits, count vowles, consonants,


# string = "Python is fun"
# rev_string = string[::-1]
# print(rev_string)

# reverse = "".join(reversed(string))
# print(reverse)

# rev_s =""
# for i in string:
#     rev_s = i+rev_s
# print(rev_s)

# r_s = " ".join(i[::-1] for i in string.split())
# print(r_s)

text = "python world is great"
reverse = " ".join(text.split()[::-1])
print(reverse) #"great is world python"

# lst = [3,4,5,"apple", "pizza", 2,1]
# print(lst[::-1])

# text = "aassddffeerrtt"
# print(text.count('d'))

# from collections import Counter
# word = "applebananacherrykiwimangomilkshake"
# print(Counter(word))

# string = "hello world"
# counts ={}
# for i in string:
#     if i in counts:
#         counts [i]+=1
#     else:
#         counts[i] =1
# print(counts)

# my_text="good boy of god"
# counts={}
# for i in my_text:
#     counts[i] = counts.get(i,0)+1
# print(counts)

# list_my = [2,4,5,2,4,5,6,72,5,6,2,3,4,72]
# simple_list = list(set(list_my))
# print(simple_list)

# sim_list = list(dict.fromkeys(list_my))
# print(sim_list)

# nums = [23,45,65,12,34, 99]
# max_num = sorted(set(nums))
# print(max_num[-2])

# #anagram
# s1 = "Sit"
# s2 = "This"

# if (sorted(s1.lower())) == sorted(s2.lower()):
#     print("True", s1, s2)
# else:
#     print("false")

# from collections import Counter
# def is_anagram(str1, str2):
#     st1= str1.lower().replace("", "")
#     st2= str2.lower().replace("", "")
#     return Counter(st1)==Counter(st2)

# print(is_anagram("dormitory", "dirty room"))
#
# num = int(input("Enter number :"))
# if num % 2 == 0:
#     print("Even")
# if num % 2 != 0:
#     print("odd")
# if num % 3 == 0 and num % 5 == 0:
#     print("num div by 3 and 5")
# else:
#     print("not div by 3 and 5")




