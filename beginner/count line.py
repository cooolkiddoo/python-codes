string=raw_input("Enter string:")
char=0
word=1
for a in string:
      char=char+1
      if(a==' '):
            word=word+1
print("Number of words in the string:")
print(word)
print("Number of characters in the string:")
print(char)
