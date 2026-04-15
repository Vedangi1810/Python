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
