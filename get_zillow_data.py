
import requests
import json
import locale
from xml.etree import ElementTree
#import webbrowser as web
locale.setlocale( locale.LC_ALL, 'en_US' )


# Property Address
address = input('Address:')#input.get('address')
city = input('city:')#input.get('city')
state = input('state:')#input.get('state')
zip  = input('zip:')#input.get('zip')

full_address = address+', '+city+' '+state+', '+zip
# Zillow API Configuration
zurl0 = 'http://www.zillow.com/webservice/'
zkey = 'YOU KEY'
zurl1 = zurl0 +'GetSearchResults.htm?zws-id='
zurl2 = '&address='
zurl3 = '&citystatezip='
citystatezip = city+' '+state+' '+zip
zurl = zurl1+zkey+zurl2+address+zurl3+citystatezip


def get_zurl(zurl):
    # Call API General
    response = requests.get(zurl)
    root = ElementTree.fromstring(response.text)
    root_status_err = root[1][0].text
    root_status = root[1][1].text

    if root_status == '501':
        print('Error: '+root_status_err)
    elif root_status == '508':
        print('Error: '+root_status_err)
    elif root_status == '0':

        # Get Variables
        zpid = root[2][0][0][0].text

        # Call API Property Details
        zurl2 = zurl0+'GetUpdatedPropertyDetails.htm?zws-id='+zkey+'&zpid='+zpid
        response2 = requests.get(zurl2)
        root2 = ElementTree.fromstring(response2.text)
        root2_status_err = root2[1][0].text
        root2_status = root2[1][1].text

        # web.open_new(zurl2)

        if root2_status == '500':
            print('Error: '+root2_status_err)
        elif root2_status == '502':
            print('Error: '+root2_status_err)
        elif root2_status == '0':

            bedrooms = root2[2][5][1].text
            bathrooms = root2[2][5][2].text
            finishedSqFt = root2[2][5][3].text
            lotSizeSqFt = root2[2][5][4].text
            yearBuilt = root2[2][5][5].text

            payload = {\
                "customSqft" : finishedSqFt\
                ,"customBathrooms" : bathrooms\
                ,"customBedrooms" : bedrooms\
                ,"customLotSize" : lotSizeSqFt\
                ,"yearBuilt" : yearBuilt\
            }
            return payload
try:
    get_zurl(zurl)
except:
    pass
