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
                continue
            elif(cap.isupper() == True):
                if(not words[2][0].isupper):
                    continue
                else:
                    spacedWords = spacedWords+" "+cap
            else:
                spacedWords += cap   


    # elif 'C' in words[1]:
    #         for cap in words[2]:
    #             continue
                    
    resulS = spacedWords.lower().strip()
    print(resulS)



        
    if "C" in words[0]:
        count = len(words[2])
        if "V" in words[1]:
            for num in range(1,count-1):
                print(words[num] + " ")
    




        elif("M" in words[1]):
            continue


        
        
        else:
            continue





        
    
    




    
    
    
    
    
    
    
    
    
    
    
