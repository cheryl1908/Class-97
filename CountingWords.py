intro=input("Introduce Yourself")
print(intro)

wordCount=1
charCount=0

for i in intro:
    charCount=charCount+1
    if i==' ':
        wordCount=wordCount+1

print("Number of words in the string:",wordCount)
print("Number of characters in the string;",charCount)
