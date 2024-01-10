str1 = "Hello"
str2 = "World"
text = str1+ " " +str2
print(text)
uppercase = text.upper()
lowercase = text.lower()
print("Uppercase:", uppercase ,"Lowercase:", lowercase)
print("Length of the string:", len(text))
new_text = text.replace("Hello", "Great")
print("Modified text:", new_text)
words = text.split()
print("Words:", words)
stripped_text = text.strip()
print("Stripped text:", stripped_text)
substring = "World"
if substring in text:
    print(substring, "found in the text")
num1 = 5.0
num2 = 2.5

# Basic Arithmetic
result1 = num1 + num2
print("Addition:", result1)

result2 = num1 - num2
print("Subtraction:", result2)

result3 = num1 * num2
print("Multiplication:", result3)

result4 = num1 / num2
print("Division:", result4)

# Rounding
result5 = round(3.14159265359, 2)  # Rounds to 2 decimal places
print("Rounded:", result5)

num1 = 10
num2 = 5

# Integer Division
print(num1,num2)
result1 = num1 // num2
print("Integer Division:", result1)

# Modulus (Remainder)
result2 = num1 % num2
print("Modulus (Remainder):", result2)

# Absolute Value
result3 = abs(-7)
print("Absolute Value:", result3)

print("#########################")

import re

text = "The quick brown fox"
pattern = "brown"

search = re.search(pattern, text)
if search:
    print("Pattern found:", search.group())
else:
    print("Pattern not found")

match = re.match(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("No match")

replacement = "red"

new_text = re.sub(pattern, replacement, text)
print("Modified text:", new_text)


text = "apple,banana,orange,grape"
pattern = r","

split_result = re.split(pattern, text)
print("Split result:", split_result)
