import json

data = {}
data['students'] = []
data['students'].append({
    'name': 'Christian Brake',
    'GitHubID': 'brake-christian',
    'NetID': 'brake.christian'
})

with open('identity.txt', 'w') as outfile:
    json.dump(data, outfile)