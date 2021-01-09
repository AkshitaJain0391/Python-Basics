#Crypotographic Examples:
import string

#Inputs from User
userString = input("Please enter your String : \n")
print(userString)

#Creating dictionary for cryptology (alphabets to numbers)
alphabet_string = string.ascii_lowercase
alphabet_list = list(alphabet_string)
AlphatoNum = dict()
for i in range(len(alphabet_list)):
    AlphatoNum.update({alphabet_list[i] : i})
AlphatoNum.update({" " : '26'})
AlphatoNum.update({'!' : '27'})
AlphatoNum.update({'?' : '28'})
print(AlphatoNum)
rawData = ""
NumtoAlpha = dict()
for i in range(len(alphabet_list)):
    NumtoAlpha.update({i: alphabet_list[i]})
NumtoAlpha.update({26 : " "})
NumtoAlpha.update({27:'!'})
NumtoAlpha.update({28:'?'})
print(NumtoAlpha)
#Chnaging the string to a cryptic message
for j in range(len(userString)):    
    k = AlphatoNum[userString[j]]       
    if int(AlphatoNum[userString[j]]) < 23 :
        for alpha, num in AlphatoNum.items():
            if num == int(AlphatoNum[userString[j]])+3:
                
                print(alpha, num)
                print(num)  
                rawData += alpha
                
    else :
        rawData += userString[j]
        pass
           
print(rawData)
print(userString)

