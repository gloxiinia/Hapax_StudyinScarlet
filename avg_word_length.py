'''
Write a program that will calculate the average word length of a text stored in a file (i.e the sum of all the lengths of the 
word tokens in the text, divided by the number of word tokens). [open http://www.gutenberg.org/ and download an 
e-book as plain text, use the file for texting your program]

'''
#import the string module
import string
#The instructions didn't require user input, but i feel like giving a user input can add more use to the program
user_file = input('Enter a text file you\'d like to calculate the average word length of (no need for the .txt):')

#opening the .txt file
open_file = open(f'{user_file}.txt', 'r')

#converting the .txt file into a str
words_file = open_file.read()

#removing the punctuation from the .txt file
punct_removed = words_file.translate(str.maketrans('', '', string.punctuation))

#removes the whitespaces and linebreaks
no_space= punct_removed.replace(" ", "").replace('\n', '')

#calculating the sum of all the lengths of the words
sum_length = len(no_space)

#splits the .txt into individual words
split_text = punct_removed.split()

#calculating the number of words in the .txt
word_total = len(split_text)

#calculating the average word length
avg_w_lgt = sum_length / word_total

print('After a long and tedious process, your text\'s average word length is...', "{:.3f} characters".format(avg_w_lgt), sep='\n')









