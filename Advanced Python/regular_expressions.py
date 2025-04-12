'''Regular Expressions in Python'''


'''Basic Matching in Python (grep or RegEx)'''
#First we import the RegEX module in Python
import re
#We then state the text we would like to be used to find a pattern
text = "Hello, my name is John Doe."
#After we decide the pattern we would like to search
pattern = "John"
# Use the RegEx module to search pattern in text - This case "John" will be searched through the text
match = re.search(pattern, text)
# fix conditions to return values if there is a match.
if match:
    print("Match Found:", match.group())
else:
    print("No Match")
#  Output ---> Match Found : John


# using the python core for finding patterns:

log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing Package Upgrade"
# Log contains the following:
# 1. Timestamp
# 2. Process name
# 3. Process ID
# 4. Error Type
# 5. Error message

# using the left square bracket will find the first square bracket available in the text

index = log.index("[")
print(log[index+1:index+6]) # this is traditional way of finding a pattern in text.

# Output --- > 12345

# These values or text can change in a log, therefore we must use a different process:

'''Using Regular Expression for the example above'''

log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing Package Upgrade"
regex = r"\[(\d+)\]" # captures one or more digits using \d+ inside the []
result = re.search(regex, log)
print(result[1])

#Output --- > 12345

'''Simple Matching in Python'''

# for checking if a string starts with a pattern we use
# re.match()

text = "Python is fun"
match = re.match("Python", text) # only checks if the string starts with "Python"
if match:
    print("Matched: ", match.group())

#Output --- > Matched: Python


'''Wildcard and Classes'''

# the dot(.) wildcard - matches any character except newline

pattern = "c.t"  # matches any three-letter word where the first is "c" and last is "t"
text = "cat cut cot"
matches = re.findall(pattern, text)
print(matches)

#Output --- > ['cat','cut','cot']

'''Character Classes'''

pattern = "c[auo]t"  # using [auo] matches any one of "a", "u", "o" between "c" and "t"
text = "cat cut cot cit cet"
matches = re.findall(pattern, text)
print(matches)

#Output --- > ['cat'.'cut','cot']

'''Repetition Qualifiers'''

# The star (*) - 0 or more occurences
# The plus sign (+) - 1 or more occurences
# The question mark (?) - 0 or 1 occurence
# {n,m} - between "n" and "m" occurences

pattern = "ab*c" # "b" can appear 0 or more times
text = "ac abc abbc abbbc"
matches = re.findall(pattern, text)
print(matches)
# b* allows "b" to be repeated multiple times (or absent)


''' Trying out advanced python expressions'''

# For Linux we use the grep function
# say we have a directory called /usr/share/dict/words and we want to match certain words
# we will look for the pattern "thon"
''' 
 grep thon /usr/share/dict/words
 
 output:
 Py*thon*
 doph*thon*
 mara*thon*
 tele*thon*
 
 when passing through grep, we need to be case sensitive

 to pass a string regardles of the case, we use "-i" parameter

 grep -i Python /usr/share/dict/words

 output:
 Python
 python
 Python's
 python's

 using the Dot(.) method to search for patterns:

 grep l.rts /usr/share/dict/words

 output:
 alerts
 blurts
 flirts

 The dot(.) pattern will substitute it with a letter

 Special characters used in Linux:
 The dollar sign ($) - Indicates the end of a line
 The circumflex(^) - Indicates the start of a line

 If we would like to find the words that start with the string "fruit" we would apply the (^).
 grep ^fruit /usr/share/dict/words

 output:
 fruit
 fruits
 fruitcake
 fruitful

 If we would like to look for words that end with "cat" we would apply ($)
 grep cat$ /usr/share/dict/words

 Output:
 Muscat
 bobcat
 cat
 copycat


'''

'''Capturing Groups'''

result = re.search(r"^(\w*),(\w*)$", "Lovelace, Ada")
print(result)

print(result.group())

