'''
A hapax legomenon (often abbreviated to hapax) is a word which occurs only once in either the written record of a 
language, the works of an author, or in a single text. Define a function that given the file name of a text will return all its 
hapaxes. Make sure your program ignores capitalization. [open http://www.gutenberg.org/ and download an e-book 
as plain text, use the file for texting your program]

'''
import string

def countWords(user_file):
    myDict = {}
    varName = open( user_file , "r")
    file = varName.read()
    punct = file.translate(str.maketrans('', '', string.punctuation))
    splitWords = punct.lower().split()
    for word in splitWords:
        myDict[word] = myDict.get(word,0)+1

    hapaxes = list(filter(lambda x: splitWords.count(x) == 1, splitWords))
    return hapaxes

        
hapax_legomenon = input("Enter a file name please:")
myWordCount = print(countWords(hapax_legomenon))


