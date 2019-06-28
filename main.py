import time
import json

with open('data.json', 'r') as json_file:
    data = json.load(json_file)

    for p in data['routine']:

        seconds = p['time']
        print(p['time'])

        print(p['title'])
        print(p['description'])

        for i in range(seconds):
            print(str(seconds - i) + " seconds remain")
            time.sleep(1)

print('Stretches now complete')
