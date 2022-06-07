# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import json
import os

import requests


def send_request(url, payload, path):
    files = {
        'messageBody': (None, json.dumps(payload), 'application/json'),
        'uploadFile': (os.path.basename(path), open(path, 'rb'), 'application/octet-stream')
    }
    return requests.post(url, files=files).content


if __name__ == '__main__':
    payload = {"id": "testId", "email": "test@test.com"}
    response = send_request(url='http://localhost:8080/upload', payload=payload, path='/Users/junhwan/Desktop/busybox')
    print(response)

