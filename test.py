from requests import *

message_id = 0

while True:
    current_message_id = message_id
    api_req = 'https://api.telegram.org/bot6696580880:AAEU6WHtuFKMz3pl79Il-tonynRFLqbEvvY'

    updates = get(api_req + '/getUpdates?offset=-1').json()

    print(updates)

    message = updates['result'][0]['message']

    chat_id = message['from']['id']
    text = message['text']
    message_id = message['message_id']

    if current_message_id != message_id:
        send_message = get(f'{api_req}/sendMessage?chat_id={chat_id}&text={text}')



