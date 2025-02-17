import urllib.request, urllib.parse, urllib.error
import json, ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

serviceurl = 'https://py4e-data.dr-chuck.net/opengeo?'

while True:
  location = input("Enter location: ")
  if (len(location) < 1): break

  location = location.strip()

  param = {"q" : location}
  serviceurl += urllib.parse.urlencode(param)

  getInfo = urllib.request.urlopen(serviceurl, context=ctx).read()
  
  try:
    js = json.loads(getInfo)
  except:
    js = None
    print("Found nothing!")

  print(js["features"][0]["properties"]["plus_code"])
  
