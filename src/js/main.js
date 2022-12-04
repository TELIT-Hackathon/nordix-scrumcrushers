import data from '../../result.json' assert { type: 'json' };
import main_data from '../../data.json' assert {type: 'json'};


let j = []
j.push(data);

j.sort(function(a, b){
    return a.value - b.value;
})
console.log(j)
let result = []

    for (let i = 0; i < j.length; i++) {
        let obj = j[i];
        for (let key in obj) {
            let value = obj[key];
            for(let x=0;x<main_data.length; x++) {
            if(value['name'] === main_data[x]['summary']['name']){
                result.push(main_data[x]['summary'])
            }
            }
        }
    }

console.log(result)
