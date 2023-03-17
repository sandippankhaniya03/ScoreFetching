import requests
from bs4 import BeautifulSoup
from pynput import keyboard

def get_scorecard():
    
    url = 'https://www.cricbuzz.com/live-cricket-scores/60028/aus-vs-ind-4th-test-australia-tour-of-india-2023'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    details = soup.select('.cb-col .cb-col-67 .cb-scrs-wrp')
    for i in details:
        print(i.getText())


keyboard.HotKey('F1',get_scorecard())

# on_press(key=keyboard.Listener)
