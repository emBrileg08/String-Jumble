"""
stringjumble.py
Author: emBrileg08
Credit: Used this link: https://stackoverflow.com/questions/5618878/how-to-convert-list-to-string
to figure out how to make a list a string
Used this link: https://stackoverflow.com/questions/15418561/convert-a-word-to-a-list-of-chars
to figure out how to convert a string into a list of individual words

Assignment:

The purpose of this challenge is to gain proficiency with 
manipulating lists.

Write and submit a Python program that accepts a string from 
the user and prints it back in three different ways:

* With all letters in reverse.
* With words in reverse order, but letters within each word in 
  the correct order.
* With all words in correct order, but letters reversed within 
  the words.

Output of your program should look like this:

Please enter a string of text (the bigger the better): There are a few techniques or tricks that you may find handy
You entered "There are a few techniques or tricks that you may find handy". Now jumble it:
ydnah dnif yam uoy taht skcirt ro seuqinhcet wef a era erehT
handy find may you that tricks or techniques few a are There
erehT era a wef seuqinhcet ro skcirt taht uoy yam dnif ydnah
"""
text=input("Please enter a string of text (the bigger the better): ")
print('You entered "'+str(text)+'". Now jumble it:')
letrev=list(text[::-1]) #converts the text into a list of letters, then reverses the order
letrevstring= ''.join(letrev) #converts the previous list into a string
print(letrevstring) #prints the string
word=text.split(" ") #Splits the inputted text into a list where each word is an item in the list
wordrev=word[::-1] #reverses the order of the previous list
wordrevstring=' '.join(wordrev) #makes the previous list a string
print(wordrevstring)
third=[(''.join(list(x[::-1]))) for x in word] #Uses the split word list, splits each word in the list into its characters, reverses the characters, then joins each list of characters back into a string
thirdstr=' '.join(third) #Stringifys the previous
print(thirdstr)