
print("terms")
puzzle="VNSSALCTTYKXAOGJVWDDEDEYRINPNJLLXTRXITIILZBDUTYYACRYNURBWEPVBNTTODILEGQZLUSDNRETGTXPEFVVTIVXYBPLPYWTMNRDTZERTBAMTMKPENKPRRJZZPLKMFQB"
c=0
print(puzzle)
print("word lists")
word_list="index","variable","function","def","len","print","class","double","attribute"
clue_list="the location of a charactor in a string","used to store information of any type","used to call and store repetitive code","starts a function dEFNITION","gets lenght of string","sends text to terminal", "a code envelope","stores double the normal integer max","a value of a object"
print(word_list)
def display_puzzle():
    print("  012345678910")
    print("0 "+puzzle[0:11])
    print("1 "+puzzle[12:23])
    print("2 "+puzzle[24:35])
    print("3 "+puzzle[36:47])
    print("4 "+puzzle[48:59])
    print("5 "+puzzle[60:71])
    print("6 "+puzzle[72:83])
    print("7 "+puzzle[84:95])
    print("8 "+puzzle[95:107])
    print("9 "+puzzle[108:119])
    print("10"+puzzle[120:131])
display_puzzle()
word2=""
e=10
z=0
attempts = 1
word1=input("enter the index positions of "+clue_list[0])
word2=word1.split(",")
word2 = list(map(int, word2))
i=0
foundword = ""
while z<11:
    print("score = " ,e)
    while i<len(word_list[z]):
        index=word2[i]
        index=int(index)
        foundword = foundword+puzzle[index]
        
        
    foundword = foundword.lower
    if foundword in word_list:
        display()
    else: attempts = attempts+1
    word1=input("enter the index positions of "+"a"+clue_list[1]+" split by commas")
    word2=word1.split(",")
    word2 = list(map(int, word2))
    i=0
    foundword = ""
def display():
    e = e+(100/attempts)
    attempts = 1
    z=z+1
    score = str(e)
    print("score = " +score+" you've got a word: ",foundword)
    


input("press enter to exit")
