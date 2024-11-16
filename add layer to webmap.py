import argparse
from arcgis.gis import GIS
from arcgis.mapping import WebMap


def main():

    print(f'Running on {args.destinationWebMapItemID} \n')
    addLayer(args.gisUrl, args.username, args.password, args.destinationWebMapItemID, args.layer_name)

def addLayer(gisUrl, username, password, destinationWebMapItemID, layer_name):
    gis = GIS(gisUrl, username, password)
    wm_item = gis.content.get(destinationWebMapItemID)
    wm = WebMap(wm_item)

    content_search= gis.content.search(layer_name)[0]
    wm.add_layer(content_search.layers[0])

    wm.update()

def parseArguments():

        parser = argparse.ArgumentParser()
        parser.add_argument('--gisUrl', dest='gisUrl', help='URL of GIS (Portal or ArcGIS Online)', required=True)
        parser.add_argument('--username', dest='username', help='GIS organization username', required=True)
        parser.add_argument('--password', dest='password', help='GIS organization password', required=True)
        parser.add_argument('--destinationWebMapItemID', dest='destinationWebMapItemID', help='Item ID of WebMap to update', required=True)
        parser.add_argument('--layer_name', dest='layer_name', help='Name of newly configured layer', required=True)
        return parser.parse_args()

if __name__ == '__main__':

        args = parseArguments()
        main()