import requests
from akamai.edgegrid import EdgeGridAuth, EdgeRc
from urllib.parse import urljoin

edgerc = EdgeRc('~/.edgerc')
section = 'default'
baseurl = 'https://{}'.format(edgerc.get(section, 'host'))

s = requests.Session()
s.auth = EdgeGridAuth.from_edgerc(edgerc, section)
s.params = {"accountSwitchKey":"B-F-JOGRRP"}

result = s.get(urljoin(baseurl,"/appsec/v1/configs"))
print(result.status_code)
print(type(result))

for list in result.json()["configurations"]:
    print("Config Name: {}".format(list['name']))
    configId = list['id']
    versionNumber = list['productionVersion']
    result_policy = s.get(urljoin(baseurl,"/appsec/v1/configs/{}/versions/{}/security-policies".format(configId,versionNumber)))

#print(dict1['configurations'][54]['name'])





