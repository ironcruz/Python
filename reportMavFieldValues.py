from lxml import etree
from pathlib import Path
import csv

# Add fields as parameter
fields = [
  'NETWORK_ROUTE_ID',
  'FROM_NETWORK_ROUTE_ID',
  'TO_NETWORK_ROUTE_ID',
  'SITE_ID',
  'COMPANY_ID'
]

# Add attributes as parameter
attributes = [
  'Searchable',
  'Visible'
]

# Add sitesfolder as parameter
sitesFolder = Path('G://Sites')

with open('ShellScripts/Output/report.csv', 'w', newline='') as report:

  reportWriter = csv.DictWriter(report, fieldnames=['MAV', 'Layer', 'Field', 'Searchable', 'Visible'])
  reportWriter.writeheader()

  for f in sitesFolder.iterdir():
    if f.name.startswith('2_'):

      try:
        tree = etree.parse((f / 'Site.xml').as_posix())
      except OSError:
        continue

      root = tree.getroot()

      mav = root.attrib['DisplayName']
      previousMav = None
      for mapService in root.findall('Map/MapServices/MapService'):
        for layer in mapService.findall('Layers/Layer'):
          for field in layer.findall('Fields/Field'):
            if field.attrib['Name'] in fields:
              reportDict = {}

              if previousMav is None or previousMav != mav:
                reportDict['MAV'] = mav
                previousMav = mav

              reportDict['Layer'] = layer.attrib['Name']
              reportDict['Field'] = field.attrib['Name']
              reportDict['Searchable'] = field.attrib['Searchable']
              reportDict['Visible'] = field.attrib['Visible']

              reportWriter.writerow(reportDict)

