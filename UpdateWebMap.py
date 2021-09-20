import requests
import json


class Updater:

    def __init__(self, webMapItemID, token, url):
        self.webmapItemID = webMapItemID
        self.token = token
        self.itemUrl = f'{url}/portal/sharing/rest/content/items/'
        print(self.itemUrl)

    def getWebMapItem(self, itemUrl, webMapItemId, token):
        itemUrl = self.itemUrl + f'{webMapItemId}?f=json&token={token}'
        r = requests.get(itemUrl)
        webMapJson= r.json()

        return webMapJson['title']

    def getWebMapData(self, webMapItemID, token):
        title = self.getWebMapItem(self.itemUrl, webMapItemID, token)
        self.dataUrl = self.itemUrl + f'{self.webmapItemID}/data?f=json&token={token}'
        r = requests.get(self.dataUrl)
        mapJson = r.json()
        json_object = json.dumps(mapJson)
        local_updateFile_path = f'some path'
        with open(local_updateFile_path,"w") as outfile:
            outfile.write(json_object)
        #print(mapJson)
        return mapJson

    def updateWebMap(self, webMapItemID, token, updateFilePath):

        with open(updateFilePath, 'r') as read:
            data = json.load(read)
            dump = json.dumps(data)
        params = {'token': token,
                'text': dump,
                'referer': f'{url}'}

        updateUrl = f'{url}/portal/sharing/rest/content/users/{username}/items/{webMapItemID}/update'
        print(updateUrl)
        update = requests.post(updateUrl, params)