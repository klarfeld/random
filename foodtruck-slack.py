#!/usr/bin/env python

from pyslack import SlackClient
import requests
from BeautifulSoup import BeautifulSoup

slack_token = 'get-ur-own'
client = SlackClient(slack_token)
url = 'https://www.gfoodtrucks.com/kiosklanding/all'

r = requests.get(url)
soup = BeautifulSoup(r.content)
today = soup.find('div', {'id': 'tab_0'})
message = ''
for box in today.findAll('div', {'class': 'ordering_box'}):
  truck_name = box.find('strong').string
  truck_type = box.find('span').string
  message = message + truck_name.strip() + " : " + truck_type.strip() + '\n'

client.chat_post_message('#sfo', message, username='foodtruckbot')


