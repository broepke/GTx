import string
import collections

punct = string.punctuation
print(punct)

my_text = open("text.txt", "r")

for line in my_text:
      line_list = line.split()

print({word:True for word in my_text})


my_text.close()