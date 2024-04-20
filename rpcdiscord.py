from pypresence import Presence
import time

client_id = '1231037839261569065'
RPC = Presence(client_id)
RPC.connect()

messages = [
    "I'm not online.",
    "I only go in at night.",
    "Have a great day! :)"
]

try:
    while True:
        for message in messages:
            RPC.update(state=message, start=time.time())
            time.sleep(3)
except KeyboardInterrupt:
    RPC.close()