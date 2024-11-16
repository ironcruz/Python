import argparse
import requests
from arcgis.gis import GIS

class DeleteProtection:
    """This class will search through specified
    Portal items for services with Delete Protection
    enabled and switch setting to specified condition."""

    def __init__(self, gisURL, username, password, ItemID, condition, token=None):
        self.gisURL = gisURL
        self.username = username
        self.password = password
        self.ItemID = ItemID
        self.condition = condition
        self.token = token

    def setDeletSettings(self):
        try:
            print(self.condition)
            objGIS = GIS(self.gisURL, self.username, self.password)
            self.token = objGIS._con.token
            print(f"Logged into Portal as {self.username} \n")
            print(f"Setting service properties to {self.condition}")
            service = objGIS.content.get(f"{self.ItemID}")
            if self.condition == "disable":
                service.protect(enable = False)
            else:
                service.protect(enable = True)
        except:
            print(f"Please verify that the item id you entered is correct")

    def setAuthoritative(self):
        print(f"{self.condition} applying to {self.ItemID}")
        set_status_url = f'{self.gisURL}/sharing/rest/content/items/{self.ItemID}/setContentStatus'
        status = ""
        if self.condition == "disable":
            pass
        else:
            status = "org_authoritative"
        params = {'token': self.token,
            "status" : f"{status}",
            "clearEmptyFields": "true",
            "f": "json"}

        setStatus = requests.post(set_status_url, params)


def main():
    setProperties = DeleteProtection(args.gisURL, args.username,args.password,args.ItemID,args.condition)
    setProperties.setDeletSettings()
    setProperties.setAuthoritative()

def parseArguments():

    parser = argparse.ArgumentParser()
    parser.add_argument('--gisURL', dest='gisURL', help='URL of GIS (Portal or ArcGIS Online)', required=True)
    parser.add_argument('--username', dest='username', help='GIS organization username', required=True)
    parser.add_argument('--password', dest='password', help='GIS organization password', required=True)
    parser.add_argument('--ItemId', dest='ItemID', help='Portal Items ID', required=True)
    parser.add_argument('--condition', dest='condition', help='Property condition to set, enable or disable', required=True)

    return parser.parse_args()

if __name__=='__main__':
    args = parseArguments()
    main()