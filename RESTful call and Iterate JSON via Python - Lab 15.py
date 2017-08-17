import requests
import json

hostname = 'localhost'
url = 'http://%s:5000/json/cisco/routes'% hostname
username = 'student'
password = 'student'

data = requests.get(url, auth=(username, password))
format_data = data.content
json_output = json.loads(format_data)
dash = '~' * 50
print dash

#Iterate through the data by matching the desired tags and pulling the strings associates
#with the tags. . In this example we will be attaining the destination network, outgoing
#interface and routing protocol for each route. We will then print the variables as we cycle
#through the route entries.

for route in json_output['items']:
    protocol = route['routing-protocol']
    dest_net = route['destination-network']
    dest_int = route['outgoing-interface']
    print 'Protocol: %s'% protocol
    print 'Destination Network: %s'% dest_net
    print 'Destination Interface: %s'% dest_int
