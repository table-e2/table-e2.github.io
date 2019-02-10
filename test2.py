from urllib.request import urlopen

baseurl = 'https://ucd-pi-iis.ou.ad3.ucdavis.edu/piwebapi/elements/'
url = baseurl + 'E0bgZy4oKQ9kiBiZJTW7eugwBjj8KdFl6BGUWQBQVpcmaQVVRJTC1BRlxSRVNUIFBPU1RTIFRPIFBJXFJFU1QgUE9TVFMgVE8gUElcVUZMXFVGTFxXSUZJIEFDQ0VTUyBQT0lOVFM/elements'
req = urlopen(url)

import json
data = json.load(req)
for key in data['Items']:
    newurl = key['Links']['RecordedData'] + '?startTime=-1h' + '&selectedFields=Items.Items.Value'
    # print(newurl)
    req = urlopen(newurl)
    selected = json.load(req)
    last = selected['Items'][0]['Items'][-1]['Value']
    try:
        val = int(last)
        print(key['Name'], end=' ')
        print(val)
    except ValueError:
        pass