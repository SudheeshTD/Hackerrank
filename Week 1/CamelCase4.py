# # Enter your code here. Read input from STDIN. Print output to STDOUT

# import sys
# input_text = sys.stdin.read()


# lines = input_text.split('\n')

# for line in lines:
#     words = line.split(';')
#     if "S" in words[0]:
#         spacedWords = ""
#         for cap in words[2]:            
#             if (not cap.isalpha()):
#                 continue
#             elif(cap.isupper() == True):
#                 if(not words[2][0].isupper):
#                     continue
#                 else:
#                     spacedWords = spacedWords+" "+cap
#             else:
#                 spacedWords += cap   


#     # elif 'C' in words[1]:
#     #         for cap in words[2]:
#     #             continue
                    
#     resulS = spacedWords.lower().strip()
#     print(resulS)



        
#     if "C" in words[0]:
#         count = len(words[2])
#         if "V" in words[1]:
#             for num in range(1,count-1):
#                 print(words[num] + " ")
    




#         elif("M" in words[1]):
#             continue


        
        
#         else:
#             continue


# def camelCase(S):
#     word = S.split(";")
    



def camelCase(s):
    word = s.split(";")
    finalword = ""
    if(word[0] == 'S'):
        if(word[1] == 'M'):
            word[2] = word[2].replace('(',"").replace(')',"")
        
        for i in word[2]:
            if(i.isupper()):
                finalword = finalword + " " + i.lower()
            else:
                finalword = finalword + i
        finalword = finalword.strip()


    elif(word[0] == 'C'):
        words = word[2].split(" ")
        if word[1] == "V" or word[1] == 'M':
            finalword += words[0]
            for i in range(1,len(words)):
                finalword += words[i].title()
            
        if word[1] == "M":
            finalword+="()"
            
        if word[1] == "C":
            for i in words:
                finalword += i.title()

    return finalword
    

while True:
    try:
        word = input().replace('\r', '')
        result = camelCase(word)
        print(result)
    except EOFError:
        break
