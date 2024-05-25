# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys
input_text = sys.stdin.read() 
lines = input_text.split('\n')

for line in lines:

    words = line.split(';')
    if "S" in words[0]:
        spacedWords = ""
        for cap in words[2]:

            if (not cap.isalpha()):
                spacedWords
            elif(cap.isupper() == True):
                spacedWords = spacedWords+" "+cap
            else:
                spacedWords += cap   


        if words[1] is 'C':
            for cap in words[2]:

                
        resul = spacedWords.lower()
        print(resul)
                
            
        
    elif "C" in words[0]:
        newWord = line
        print(words[2])