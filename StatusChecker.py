import requests


class Checker:

    def __init__(self, service, token):
        self.token = token
        self.statusList = []
        self.service = service

    def checkStatus(self):
        r = requests.get(self.serviceUrl)
        json = r.json()
        if str(r.status_code) != '200':
            self.service['attributes']['Error'] = r.text['error']['message']
            self.service['attributes']['Status'] = 1
            self.statusList.append(self.service)

        elif "error" in json:
            self.service['attributes']['Status'] = 1
            self.service['attributes']['Error'] = json['error']['message']
            self.statusList.append(self.service)

        else:
            self.service['attributes']['Status'] = 0
            self.statusList.append(self.service)