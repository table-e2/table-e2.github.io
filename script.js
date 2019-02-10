
var addOpts = function(id, num, labels) {
    for (let i = 0; i < num; i++) {
        let node = document.createElement('option');
        node.value = i;
        let txtnode = document.createTextNode(labels[i]);
        node.appendChild(txtnode);
        document.getElementById(id).appendChild(node);
    }
};
addOpts('weekday', 7, [
    'Mon',
    'Tue',
    'Wed',
    'Thu',
    'Fri',
    'Sat',
    'Sun',
]);
addOpts('hour', 24, [
    '00',
    '01',
    '02',
    '03',
    '04',
    '05',
    '06',
    '07',
    '08',
    '09',
    '10',
    '11',
    '12',
    '13',
    '14',
    '15',
    '16',
    '17',
    '18',
    '19',
    '20',
    '21',
    '22',
    '23',
]);
addOpts('minute', 6, [
    '00',
    '10',
    '20',
    '30',
    '40',
    '50',
]);

fetch('building_list.json')
    .then(function(resp) {
        return resp.json();
    })
    .then(function(data) {
        for (let bld of data) {
            let node = document.createElement('option')
            let txtnode = document.createTextNode(bld)
            node.appendChild(txtnode)
            document.getElementById('building').appendChild(node)
        }
        let now = new Date();
        let wk = (now.getDay() + 6) % 7;
        let hr = now.getHours();
        let mn = now.getMinutes();
        mn = Math.floor(mn / 10);
        document.getElementById('weekday').value = wk;
        document.getElementById('hour').value = hr;
        document.getElementById('minute').value = mn;
    }
);

fetch('data.json')
    .then(function(response) {
        return response.json();
    }).then(function(data) {
        document.getElementById('result').innerHTML = 'Loaded';
        
        let button = document.getElementById('submit')
        button.onclick = function() {
            let bldg = document.getElementById('building').value;
            let weekday = document.getElementById('weekday').value;
            let hour =  document.getElementById('hour').value;
            let minute = document.getElementById('minute').value;
            // console.log([bldg,weekday,hour,minute]);
            let index = 0;
            index += parseInt(weekday) * 24 * 6;
            index += parseInt(hour) * 6;
            index += parseInt(minute);
            // result = document.createTextNode(data[bldg][index]);
            let days = 249 / 7;
            let devices = (data[bldg][index] / days).toFixed(1);
            document.getElementById('result').innerHTML = 'Average for this time of the week: <strong>' + devices + '</strong>';
            let sum = 0;
            for (count of data[bldg]) {
                sum += count;
            }
            let average = sum / data[bldg].length / days;
            let baseurl = 'https://ucd-pi-iis.ou.ad3.ucdavis.edu/piwebapi/elements/'
            let url = baseurl + 'E0bgZy4oKQ9kiBiZJTW7eugwBjj8KdFl6BGUWQBQVpcmaQVVRJTC1BRlxSRVNUIFBPU1RTIFRPIFBJXFJFU1QgUE9TVFMgVE8gUElcVUZMXFVGTFxXSUZJIEFDQ0VTUyBQT0lOVFM/elements'
            fetch(url).then(function(resp) {
                return resp.json();
            }).then(function(data) {
                newurl = '';
                for (key of data['Items']) {
                    if (key['Name'] == bldg) {
                        newurl = key['Links']['RecordedData'] + '?startTime=-1h' + '&selectedFields=Items.Items.Value';
                        break;
                    }
                }
                return fetch(newurl)
            }).then(function(resp) {
                return resp.json();
            }).then(function(data) {
                let len = data['Items'][0]['Items'].length;
                let last = data['Items'][0]['Items'][len - 1]['Value']
                if (isNaN(last)) {
                    console.log('Did not find value');
                    return 0;
                } else {
                    return parseInt(last);
                }
            }).then(function(last) {
                let node = 'Current devices connected: <strong>' + last + '</strong>';
                document.getElementById('current').innerHTML = node;
                let factor = (last / devices).toFixed(2);
                document.getElementById('deets').innerHTML = 'It is <strong>' + factor + '</strong> times the usual for this time of the week.' +
                '<br>This building averages <strong>' + average.toFixed(1) + '</strong> devices overall.'
            });
        };
    });