export default [

    {
        //the part after '#' in the url (so-called fragment):
        hash: "welcome",
        ///id of the target html element:
        target: "router-view",
        //the function that returns content to be rendered to the target html element:
        getTemplate: (targetElm) =>
            document.getElementById(targetElm).innerHTML = document.getElementById("template-welcome").innerHTML,
    },

    // {
    //     hash: "articles",
    //     target: "router-view",
    //     getTemplate: function,
    // }
];
