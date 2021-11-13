'''
Write a program that given a text file will create a new text file in which all the lines from the original file are numbered 
from 1 to n (where n is the number of lines in the file).

'''
#The instructions didn't require user input, but i feel like giving a user input can add more use to the program
user_file = input('Enter a text file you\'d like to number the lines of (no need for the .txt):')
#user input for the name of the new numbered .txt file
new_file_name = (input('What would you like the new file to be named as? (no need for the .txt):'))

#
#opening the .txt file to  read
open_file = open(f'{user_file}.txt', 'r')

#creating a list of all lines in the text
file_lines = open_file.readlines()

#creating a new .txt file with the numbered lines
create_file = open(f'{new_file_name}.txt', 'w')

#counter for the for loop
count = 0

#for loop to add the numbers to the beginning of each line in the .txt file
for line in file_lines:
    count += 1
    create_file.write('{:d}. {}'.format(count, line))

#closing both files after
open_file.close()
create_file.close()











