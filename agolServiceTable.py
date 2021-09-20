import requests
import json



agolURL = " "


def getServices(token):

        print(" Retrieving Features ...")

        reqUrl = f'{agolURL}/query'

        data = {
                'token':token,
                'f': 'json',
                'where':'1=1',
                'outFields':'*'
                }

        r = requests.get(reqUrl, data)

        return r.json()["features"]


def update(token, features):
        for feature in features:

                print(f'Updating Status of feature ObjectId {feature["attributes"]["OBJECTID"]}...')

                reqUrl = f'{agolURL}/applyEdits'
                updates = [feature]
                data = {
                        'f': 'json',
                        'token':token,
                        'updates': json.dumps(updates)
                        }

                r = requests.post(reqUrl, data)

                return r.json()["updateResults"]