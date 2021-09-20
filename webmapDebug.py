import configparser
import urllib.parse
from arcgis.gis import GIS
from arcgis.mapping import WebMap

config = configparser.ConfigParser()
config.read('config.ini')
gisUrl = config["ENVIRONMENT"]["portalurl"]
config.read('credentials.ini')
username, password = config["CREDENTIALS"]['portalusername'], config["CREDENTIALS"]['portalpassword']

objGIS = GIS(gisUrl, username, password)
token = objGIS._con.token
services = []

items=objGIS.content.search(query='*', item_type="Web Map", max_items=500)
for item in items:
    if hasattr(item, "contentStatus"):
        print(f'Collecting service and layer info from {item.title} \n')
        wm_item = objGIS.content.get(item.id)
        wm = WebMap(wm_item)
        try:
            for layer in wm.layers:
                
                url = layer.url
                # print(url)
                parsed = urllib.parse.urlsplit(url)
                servicename= ((parsed.path.split('/')[-4]+'/'+parsed.path.split('/')[-3] +'/'+parsed.path.split('/')[-2]) + f"/{layer.title}")
                print(servicename +'\n')
                appInfo = (wm_item.title, servicename) #empty quotes to skip the OBJECTID field
                services.append(appInfo)
        except AttributeError:
            url = layer.templateUrl
            print(url)
            parsed = urllib.parse.urlsplit(url)
            servicename= ((parsed.path.split('/')[-8]+'/'+parsed.path.split('/')[-7]) + f"/{layer.title}")
            appInfo = (wm_item.title, servicename) #empty quotes to skip the OBJECTID field
            services.append(appInfo)
    else:
        pass
