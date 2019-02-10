
var addOpts = function(id, num, interval) {
    for (let i = 0; i < num; i++) {
        let node = document.createElement('option')
        let txtnode = document.createTextNode(i * interval)
        node.appendChild(txtnode)
        document.getElementById(id).appendChild(node)
    }
};
addOpts('weekday', 7, 1);
addOpts('hour', 24, 1);
addOpts('minute', 6, 10);

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
            document.getElementById('result').innerHTML = data[bldg][index];
        };
    });
    
