# Alice wrote a sequence of words in CamelCase as a string of letters, , having the following properties:

# It is a concatenation of one or more words consisting of English letters.
# All letters in the first word are lowercase.
# For each of the subsequent words, the first letter is uppercase and rest of the letters are lowercase.
# Given s, print the number of words in s on a new line.

# For example, s=oneTwoThree . There are 3 words in the string.

s=input()
i=1
for _ in s:
    if _.isupper():
        i+=1
print(i)