'''
Your task here is to write a program that given the name of a text file can write its content with each sentence on a 
separate line. Test your program with the following short text:

Mr. Miyagi bought cheapsite.com for 1.5 million dollars, i.e. he paid a lot for it. Did he mind? Adam Jones Jr. thinks he 
didn't. In any case, this isn't true... Well, with a probability of .9 it isn't. 

The result should be:

Mr. Miyagi bought cheapsite.com for 1.5 million dollars, i.e. he paid a lot for it.
Did he mind?
Adam Jones Jr. thinks he didn't.
In any case, this isn't true...
Well, with a probability of .9 it isn't

Sentence boundaries occur at one of "." (periods), "?" or "!", except that .
Periods followed by whitespace followed by a lower case letter are not sentence boundaries.
a) Periods followed by a digit with no intervening whitespace are not sentence boundaries.
b) Periods followed by whitespace and then an upper case letter, but preceded by any of short 
list of titles are not sentence boundaries.
c) Sample titles include Mr., Mrs., Dr., and so on.
d) Periods internal to a sequence of letters with no adjacent whitespace are not sentence 
boundaries
e) (for example, www.aptex.com, or e.g).
f) Periods followed by certain kinds of punctuation (notably comma and more periods) are 
probably not sentence boundaries.

'''
#importing the regular expressions module
import re

#asking user input for the text file
user_file = input('Please input the text you\'d like to be split (no .txt needed):')
regex_file = input('Now input what you\'d like to name the formatted file (no .txt needed):')

#opening the file to read
open_file = open(f'{user_file}.txt', 'r')

#converting the file to string
words_file = open_file.read()

regex_file = open(f'{regex_file}.txt', 'w')

#Removing any line breaks
no_newline= words_file.replace('\n', '')

#creates a variable for the sub() pattern requirements
#using negative lookbehind assertion  for the titles, then a period, space, uppercase letter (name)
title = '(?<!Mr)(?<!Ms)(?<!Mrs)(?<!Mx)(?<!Dr)(?<!Sr)(?<!Jr)\.\s([A-Z])'

#Checking for titles, if they do not match the pattern, adds a new line 
check_title = re.sub(title, r'.\n\1', no_newline)

#checking for question marks (?), adds a new line if followed by a space
check_question= re.sub(r'\?\s', '?\n', check_title)

#checking for exclamation marks (!), adds a new line if followed by a space
check_exclaim = re.sub(r'\!\s', '!\n', check_question)


#Decided to create a new .txt file so the finished result is displayed neater when working with larger blocks of text
#creating a new text file with the results of the formatted file
regex_file.write(check_exclaim)

#closing both files
open_file.close()
regex_file.close()















