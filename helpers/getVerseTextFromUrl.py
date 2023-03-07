from bs4 import BeautifulSoup
import urllib.request

def getVerseTextFromUrl(url):
    class AppURLopener(urllib.request.FancyURLopener):
        version = "Mozilla/5.0"

    opener = AppURLopener()
    response = opener.open(url)
    data = response.read()

    soup = BeautifulSoup(data, 'html.parser')
    verseText = soup.find("div", class_="yv-gray50")

    if verseText.text == 'Book':
        raise Exception('Must enter a valid Bible reference')
    
    return verseText.text