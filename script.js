
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
    }
);

fetch('data.json')
    .then(function(response) {
        return response.json();
    }).then(function(data) {
        document.getElementById('result').innerHTML = '';
        
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
            document.getElementById('result').innerHTML = 'Historical devices: ' + devices;
            let sum = 0;
            for (count of data[bldg]) {
                sum += count;
            }
            let average = sum / data[bldg].length / days;
            let factor = devices / average;
            document.getElementById('deets').innerHTML = 'This building usually has ' + average.toFixed(1) + 
                ' devices. It is ' + factor.toFixed(2) + ' times average.';
        };
    });
    
