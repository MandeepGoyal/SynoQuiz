
import requests
import time
import random
from lxml import html

from bs4 import BeautifulSoup

print("Hola! Welcome to the program\n")
time.sleep(2)
print("To play the WORD GAME press 1 ENTER\n")
print("To Search Word press 2 ENTER\n")
print("To exit press 0 ENTER\n")

flag1=True
while flag1:
    choose = int(input("Enter your choice: "))
    if choose==0:
        print("See you next time\n")
        break
    if choose==1:
        flag1=False
        print("You choose to play WORD GAME\n")
    elif choose==2:
        print("You choose to search a word\n")
        flag1=False
    else:
        print("Invalid input")

def search_word(word):
    URL = "https://api.dictionaryapi.dev/api/v2/entries/en/" + word
    x = requests.get(URL)
    data = x.json()

    if type(data)!=list:
        return "Not Valid\n"
    
    synonym_list=set()
    for a in data:
        for i in a["meanings"]:
            for j in i["synonyms"]:
                synonym_list.add(j)
            
    antonym_list=set()
    for a in data:
        for i in a["meanings"]:
            for j in i["antonyms"]:
                antonym_list.add(j)

    meaning_list=set()
    for a in data:
        for i in a["meanings"]:
            for j in i["definitions"]:
                meaning_list.add(j["definition"])

    ans=[]
    ans.append(meaning_list)
    ans.append(synonym_list)
    ans.append(antonym_list)
    return ans

def play_game(exam):
    if exam=="GRE":
        URL="https://www.vocabulary.com/lists/194479#view=list"
    if exam=="GMAT":
        URL="https://www.vocabulary.com/lists/197265#view=list"
    if exam=="SAT":
        URL="https://www.vocabulary.com/lists/191545#view=list"
    req = requests.get(URL)
    soup = BeautifulSoup(req.content,"html.parser")
    res = soup.find_all('a', class_ = "word")
    all_word=[]
    for i in res:
        all_word.append(str(i.text))
    word_arr=random.choices(all_word,k=10)
    #return word_arr
    # Now we have the words that need to be asked from player
    score=0
    wrong_ans=[]
    word_meanings=[]
    word_synonyms=[]
    for i in range(10):
        ans=input("Enter SYNONYM of "+word_arr[i]+": ")
        results=search_word(word_arr[i])
        #print(results)
        if ans in results[1]:
            score=score+1
            print("Correct!")
        else:
            print("Oops! Wrong Answer.")
            wrong_ans.append(word_arr[i])
            word_meanings.append(results[0])
            word_synonyms.append(results[1])
    if score==10:
        print("Perfect>>>")
        print("Score: "+ str(score)+"\n")
    else:
        print("Your Score: "+str(score))
        print("Meanings of the wrong answers and synonyms are below\n")
        for i in range(len(wrong_ans)):
            print("Word: "+wrong_ans[i])
            print("Word meanings>>>")
            print(word_meanings[i])
            print("Word synonyms>>>")
            print(word_synonyms[i])

#print(play_game("GRE"))

if choose==1:
    # we are going to play the game
    while True:
        print("There are 3 games available.\n")
        print("Press 1 ENTER for GRE")
        print("Press 2 ENTER for GMAT")
        print("Press 3 ENTER for SAT")
        choice=int(input("\nENTER your choice: "))

        if choice==1:
            play_game("GRE")
        if choice==2:
            play_game("GMAT")
        if choice==3:
            play_game("SAT")
        another_game = input("Wanna play another game? Yes or No: ")
        if another_game=="No":
            print("Game Ended.\n")
            break

if choose==2:
    # we are going to search the word
    while True:
        word = input("Enter your word: ")
        print("")
        if word=="q":
            print("Word Search ended\n")
            break
        data = search_word(word)
        if type(data)==str:
            print(data)
            continue
        print("******************************Definions******************************\n")
        for i in data[0]:
            print(i+"\n")
        print("******************************Synonyms******************************\n")
        for i in data[1]:
            print(i+"\n")
        print("******************************Antonyms******************************\n")
        for i in data[2]:
            print(i+"\n")
        
