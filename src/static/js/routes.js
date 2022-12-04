import Mustache from "../js/mustache.js";
import data from '../../result.json' assert {type: 'json'};
import main_data from '../../data.json' assert {type: 'json'};

export default function result_sort() {
    let j = []
    j.push(data);

    j.sort(function (a, b) {
        return a.value - b.value;
    })
// console.log(j)
    let result = []

    for (let i = 0; i < j.length; i++) {
        let obj = j[i];
        for (let key in obj) {
            let value = obj[key];
            for (let x = 0; x < main_data.length; x++) {
                if (value['name'] === main_data[x]['summary']['name']) {
                    // result.push(main_data[x]['summary'])
                    let name = main_data[x]['summary']['name'];
                    let logo = main_data[x]['summary']['logo'];
                    let rating = main_data[x]['summary']['rating'];
                    let numOfReviews = main_data[x]['summary']['noOfReviews'];
                    let description = main_data[x]['summary']['description'];
                    let minProjectSize = main_data[x]['summary']['minProjectSize'];
                    let avgHourlyPay = main_data[x]['summary']['averageHourlyPay'];
                    let employees = main_data[x]['summary']['employees'];
                    let founded = main_data[x]['summary']['founded'];

                    const newArticle =
                        {
                            name: name,
                            logo: logo,
                            rating: rating,
                            noOfReviews: numOfReviews,
                            description: description,
                            minProjectSize: minProjectSize,
                            averageHourlyPay: avgHourlyPay,
                            employees: employees,
                            founded: founded
                        };

                    result.push(newArticle)
                }
            }
        }
    }

    Mustache.render(document.getElementById('template-articles').innerHTML, result.slice(5))
}

[

    {
        //the part after '#' in the url (so-called fragment):
        hash: "welcome",
        ///id of the target html element:
        target: "router-view",
        //the function that returns content to be rendered to the target html element:
        getTemplate: (targetElm) =>
            document.getElementById(targetElm).innerHTML = document.getElementById("template-welcome").innerHTML,
    },

    {
        hash: "articles",
        target: "router-view",
        getTemplate: result_sort
    }
];


// function fetchAndDisplayArticles() {
//     let opinionsFromStorage = result_sort();
//     for (let i = 0; i < opinionsFromStorage.length; i++) {
//         const newOpinion =
//             {
//                 name: nopName,
//                 email: nopEmail,
//                 age: nopAge,
//                 color: nopColor,
//                 gender: nopGender,
//                 comment: nopOpn,
//                 product: nopProduct,
//                 createdDate: new Date()
//             };
//
//     }
// }