'''
Key Differences:
re.match(): Matches only from the start (index 0).
re.search(): Matches the first occurrence anywhere in the string.
re.findall(): Returns a list of all occurrences found.

'''

import re
text = "my native place is solapur"
pattern = r"solapur"
match = re.match(pattern, text)
if match:
    print("match found: ", match.group())
else:
    print("No match found")

# import re
# text = "my native place is Solapur"
# pattern = r"(?i)solapur" #case-insensitive
# match = re.search(pattern, text)
# if match:
#     print("match found: ", match.group())
# else:
#     print("No match found")

# import re
text = "my native place is solapur and I live in Solapur"
pattern = r"solapur"
match = re.findall(pattern, text, re.IGNORECASE)
if match:
    print("match found: ", match)
else:
    print("No match found")

# import re
# text = "The order includes 5 apples, 12 bananas, and 1 orange."
# pattern = r"\d+"
# # Returns a list of all matches found
# numbers = re.findall(pattern, text)
# print(numbers)

#Replace
# import re
# text = "my native place is solapur and I live in Solapur"
# pattern = r"(?i)solapur"
# replace = "Pune"
# match = re.sub(pattern,replace, text)
# if match:
#     print("match found: ", match)
# else:
#     print("No match found")

import re
text = "apple,banana,orange,grape"
pattern = r","
split_result = re.split(pattern, text)
print("Split result:", split_result)

###################################################
STRING

# # string concatenation
# str1 = "vedangi"
# str2 = "dhole"
# print(str1+" "+str2)

# # string length
# strlen = "myname is vedangi"
# print(len(strlen))

# # string replace
# orgstring = "region is uat"
# repstring = "prod"
# print(orgstring.replace("uat",repstring))

# # string conversion (lowercase, uppercase)
# strcase = "Vedangi"
# print(strcase.lower())
# print(strcase.upper())

# # string split and strip
# strcut = " * welcome to python **"
# print(strcut.split(" "))

# # The argument is treated as a set of individual characters, not a specific sequence. The order of the characters in strip(" *") does not matter.
# print(strcut.strip(""))
# print(strcut.strip("p")) # strip will not remove character in between
# print(strcut.lstrip(" *"))
# print(strcut.rstrip(" *"))

# strcut2 = "** *Hello, world!!!***!!!"
# print(strcut2.strip("*! "))

# txt = ",,,,,rrttgg.....banana....rrr"

# x = txt.strip(",.grt")

# print(x) #banana

# substr = "my name is vedangi"
# if "vedangi" in substr:
#     print("Yes")

# #################################################################333333

num1 = 10
num2 = 5

print(num1 % num2)
print(num1 // num2)
print(num1 / num2)
print(abs(-85))

num3 = 5.4
num4 = 2.8
print(num3 * num4)
print(num3 + num4)
print(num3 - num4)
print(num3 / num4)
print(num3 // num4) # 1.0 floor division : rounds to nearest down value any .0 because one of the input is float so return float output
print(round(3.1425754467,2))
