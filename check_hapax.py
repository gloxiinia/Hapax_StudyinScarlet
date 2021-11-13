'''
A hapax legomenon (often abbreviated to hapax) is a word which occurs only once in either the written record of a 
language, the works of an author, or in a single text. Define a function that given the file name of a text will return all its 
hapaxes. Make sure your program ignores capitalization. [open http://www.gutenberg.org/ and download an e-book 
as plain text, use the file for texting your program]

'''
#imported the string module for formatting punctuation
import string

def countWords(user_file):
    #creates a new dictionary
    myDict = {}
    #opens the file
    open_text = open( user_file , "r")
    #converts the file into string
    file = open_text.read()
    #removes all punctuation from the .txt file
    punct_removed = file.translate(str.maketrans('', '', string.punctuation))
    #splits the .txt file and converts all eligible characters to lower case
    splitWords = punct_removed.lower().split()
    #for loop to check the occurance of a word
    for word in splitWords:
        myDict[word] = myDict.get(word,0)+1

    #Used lambda as an anonymous function along with the filter function to filter the hapaxes
    hapaxes = list(filter(lambda x: splitWords.count(x) == 1, splitWords))  

    #saving the hapaxes filtered
    return hapaxes

#asking for user .txt file input        
hapax_legomenon = input("Enter a file name please:")
#calling the functon and saving the result
myWordCount = print(countWords(hapax_legomenon))


