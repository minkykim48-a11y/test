import requests
import re
from bs4 import BeautifulSoup as bs
from datetime import datetime
import streamlit as st

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}
data = requests.get('https://dormi.kongju.ac.kr/HOME/sub.php?code=041303', headers=headers)

soup = bs(data.text, 'html.parser')

for i in range(3,6):
    tmp = soup.select_one(f'.table-board > tbody:nth-child(4) > tr:nth-child({datetime.now().day%7+1}) > td:nth-child({i})').text.replace('\n',',')
    if i == 3:
        st.write(f'아침: {tmp}')
    elif i == 4:
        st.write(f'점심: {tmp}')
    else:
        st.write(f'저녁: {tmp}')
