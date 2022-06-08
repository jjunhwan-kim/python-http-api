import requests
import os
import json

data = {
    'id': 'jjunhwan.kim',
    'email': 'jjunhwan.kim@test.com'
}


def print_request(req):
    """
    At this point it is completely built and ready
    to be fired; it is "prepared".

    However pay attention at the formatting used in
    this function because it is programmed to be pretty
    printed and may differ from the actual request.
    """
    print('{}\n{}\r\n{}\r\n\r\n{}'.format(
        '-----------START-----------',
        req.method + ' ' + req.url,
        '\r\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),
        req.body,
    ))


def send_json(url, data):
    request = requests.Request('POST', url, json=data)
    prepared_request = request.prepare()
    print_request(prepared_request)
    response = send_request(prepared_request)
    return response


def send_multipart_form_data(url, data, file):
    file = open(file, 'rb')
    files = {'uploadFile': file}

    # requests.post(url=url, data=data, json=json, file=file)
    request = requests.Request('POST', url, data=data, files=files)
    prepared_request = request.prepare()
    print_request(prepared_request)
    response = send_request(prepared_request)

    file.close()
    return response


def send_json_with_multipart_form_data(url, data, file):
    basename = os.path.basename(file)
    file = open(file, 'rb')

    files = {
        'data': (None, json.dumps(data), 'application/json'),
        'uploadFile': (basename, file, 'application/octet-stream')
    }
    request = requests.Request('POST', url, files=files)
    prepared_request = request.prepare()
    print_request(prepared_request)
    response = send_request(prepared_request)

    file.close()
    return response


def send_request(prepared_request):
    session = requests.Session()
    return session.send(prepared_request)



if __name__ == '__main__':
    response = send_multipart_form_data(url='http://localhost:8080/upload1', data=data, file='/Users/junhwan/Desktop/test.txt')
    print(response.text)

    response = send_json(url='http://localhost:8080/upload2', data=data)
    print(response.text)

    response = send_json_with_multipart_form_data(url='http://localhost:8080/upload3', data=data, file='/Users/junhwan/Desktop/test.txt')
    print(response.text)

