#Created by: Ethan Lee, September 2014
#Updated: Ethan Lee, May 2018
#Creates html file that is the compiled chapter content of the web serial "Ward"
from bs4 import BeautifulSoup
import requests

file = open("Ward.html", "w")

r = requests.get('https://www.parahumans.net/table-of-contents/')
soup = BeautifulSoup(r.content, "lxml")
stufftocut = "Previous Chapter                                                                                        Next Chapter"
comments = False
chapterlist = soup.find_all('a')

for i in range(22,125):#from table of contents go to each chapter
        r2 = requests.get(chapterlist[i]["href"])
        soup2 = BeautifulSoup(r2.content, "lxml")
        content = soup2.find_all('p')
        file.write(str(soup2.find_all('h1', class_ = "entry-title")[0]))
        print(str(soup2.find_all('h1', class_="entry-title")[0].get_text()))
        for element in content:
            text = element.get_text()
            if ("Previous" in text)and comments == False:
                #last chapter comment appears twice: before content and before comments
                comments = True
            elif ("Previous" in text)and comments == True:
                #when the second last chapter comment appears stop (b/c it is comments)
                comments = False
                break
            elif text != stufftocut:
                elementtext = (str(element))
                #replace problem symbols (emojis, shapes etc.)
                if "■" in elementtext:
                    elementtext = elementtext.replace("■","[]")
                if "►" in elementtext:
                    elementtext = elementtext.replace("►",">")
                if "♦" in elementtext:
                    elementtext = elementtext.replace("♦","X")
                if "•" in elementtext:
                    elementtext = elementtext.replace("•","o")
                if "😦" in elementtext:
                    elementtext = elementtext.replace("😦",":)")
                if "☿" in elementtext:
                    elementtext = elementtext.replace("☿", "^-_-^")
                if "😉" in elementtext:
                    elementtext = elementtext.replace("😉",":p")
                if "ō" in elementtext:
                    elementtext = elementtext.replace("ō","o")
                if "ǎ" in elementtext:
                    elementtext = elementtext.replace("ǎ","a")
                if "à" in elementtext:
                    elementtext = elementtext.replace("à","a")
                if "á" in elementtext:
                    elementtext = elementtext.replace("á", "a")
                if "ā" in elementtext:
                    elementtext = elementtext.replace("ā", "a")
                if "ì" in elementtext:
                    elementtext = elementtext.replace("ì", "i")
                if "ú" in elementtext:
                    elementtext = elementtext.replace("ú", "u")
                if "è" in elementtext:
                    elementtext = elementtext.replace("è", "e")
                if "ò" in elementtext:
                    elementtext = elementtext.replace("ò", "o")
                if "ū" in elementtext:
                    elementtext = elementtext.replace("ū", "u")
                if "ē" in elementtext:
                    elementtext = elementtext.replace("ē", "e")
                if "ě" in elementtext:
                    elementtext = elementtext.replace("ě", "e")
                if "ī" in elementtext:
                    elementtext = elementtext.replace("ī", "i")
                if "̄" in elementtext:
                    elementtext = elementtext.replace("̄", "-")
                if "⊙" in elementtext:
                    elementtext = elementtext.replace("⊙", "*")
                #add content to file, skipping junk
                if "Next" not in text and "Ward" not in elementtext:
                     try:
                         file.write(elementtext)
                     except UnicodeEncodeError:
                         #for finding cause of errors
                         print(elementtext) #prints title of chapters as they are visited

file.close