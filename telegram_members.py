from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
from telethon.tl.types import ChatForbidden
import csv
from datetime import date
from collections import OrderedDict

api_id = 3561678
api_hash = '369f403b32609b76128abdf8453fc9ca'
phone = '+2348127350135'

def print_groups(groups):
    for i in range(len(groups)):
        print_group(groups[i])

def print_group(target_group):
  print('Fetching Members...')
  all_participants = []
  all_participants = client.get_participants(target_group, aggressive=True)

  print('Saving In file...')
  with open(target_group.title+"-"+date.today().isoformat()+".csv", "w", encoding='UTF-8') as f:
      writer = csv.writer(f, delimiter=",", lineterminator="\n")
      writer.writerow(['username', 'user id', 'access hash',
                      'name', 'group', 'group id'])
      for user in all_participants:
          if user.username:
              username = user.username
          else:
              username = ""
          if user.first_name:
              first_name = user.first_name
          else:
              first_name = ""
          if user.last_name:
              last_name = user.last_name
          else:
              last_name = ""
          name = (first_name + ' ' + last_name).strip()
          writer.writerow([username, user.id, user.access_hash,
                          name, target_group.title, target_group.id])
  print('Members scraped successfully.')

client = TelegramClient(phone, api_id, api_hash)

client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code: '))


chats = []
last_date = None
chunk_size = 200
group_dict = {}
groups = []

result = client(GetDialogsRequest(
    offset_date=last_date,
    offset_id=0,
    offset_peer=InputPeerEmpty(),
    limit=chunk_size,
    hash=0
))
chats.extend(result.chats)

print("chat count:" + str(len(chats)))

for chat in chats:
    try:
        if isinstance(chat, (ChatForbidden)):
            continue
        elif "MOP" in chat.title or "NIGERIA WE MOVE" in chat.title or "Novel Nigeria Crusaders Initiative" in chat.title or "Naija Resistance Movement (NRM)" in chat.title:
            group_dict[chat.title] = chat
    except:
        continue

groups = list(group_dict.values())
groups = sorted(groups, key=lambda group:group.title)

print("group count:" + str(len(groups)))
print('Choose a group to scrape members from:')
i = 0
for g in groups:
    print(str(i) + '- ' + g.title)
    i += 1

g_index = ''
while True:
  g_index = input("Enter a Number from 0 to "+str(len(groups)-1) +": ")
  if(g_index) == 'x' or not g_index:
      break
  elif(g_index) == 'all':
      print_group(groups)
  else:
      target_group = groups[int(g_index)]
      print_group(target_group)