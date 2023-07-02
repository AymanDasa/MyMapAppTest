import urllib.request as request
import urllib.parse as parse
import json


def main():
    while True:
        address = input("Enter your address: ")
        if len(address) < 1:
            break
        git_my_location(address)


def git_my_location(address):
    server = 'https://py4e-data.dr-chuck.net/json?'
    url_parm = dict()
    url_parm['key'] = 42
    url_parm['address'] = address
    url = server + parse.urlencode(url_parm)
    response = request.urlopen(url)  # response Type: <class 'http.client.HTTPResponse'>
    response_data = response.read().decode()  # response_data Type:  <class 'str'>
    json_object = json.loads(response_data)  # response_data Type:  <class 'dict'>
    if json_object["status"] == "OK":
        print('lat', json_object['results'][0]['geometry']['location']['lat'],
              '- lng', json_object['results'][0]['geometry']['location']['lng'])
    else:
        print('Fail, or Error')


if __name__ == '__main__':
    main()
