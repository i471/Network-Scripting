import requests
import json
import xlsxwriter

hostname = 'localhost'
url = 'http://%s:5000/json/cisco/routes'% hostname
username = 'student'
password = 'student'

data = requests.get(url, auth=(username, password))
format_data = data.content
json_output = json.loads(format_data)
count = 0
workbook = xlsxwriter.Workbook('/home/student/Desktop/routes.xlsx')
worksheet = workbook.add_worksheet()
worksheet.set_column(0, 2, 24)
row = 0
col = 0

for route in json_output['items']:
      dest_net = route['destination-network']
      dest_int = route['outgoing-interface']
      protocol = route['routing-protocol']
      worksheet.write(col + count, row, protocol)
      worksheet.write(col + count, row + 1, dest_net)
      worksheet.write(col + count, row + 2, protocol)
      count = count + 1
workbook.close()
