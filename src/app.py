from flask import Flask, render_template, request, render_template_string
from sort import MainSort


app = Flask(__name__, template_folder="./templates")


@app.route('/')
def render():
    return render_template("index.html")


@app.route('/', methods=['POST'])
def input_data():
    if request.method == 'POST':
        data = request.form['input_name']
        main_sort = MainSort(str(data))
        sort_d = main_sort.sort_data(20, 5)
        return render_template_string("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Nordix Challenge</title>
    <link rel="stylesheet" href="../static/css/style.css">
    <link rel="stylesheet" href="../static/css/normalize.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Dancing+Script">
</head>
<body>
<main id="router-view">
    <script>
        function showBtn(textarea) {
            let isOn = false;
            let button = document.getElementsByClassName("fancyButton")[0]
            // let textarea = document.getElementsByClassName("searchSpace")[0]
            textarea.oninput = function () {
                if (this.value === "") {
                    button.classList.toggle("changeButton")
                    isOn = false;
                    return
                }
                if (!isOn) {
                    button.classList.toggle("changeButton")
                    isOn = true;
                }
            }
        }
    </script>
</main>
</body>
</html>

<template id="template-welcome">
        <h2 class="homeText">Scrum Crushers</h2>

    <form method="post">
        <input oninput="showBtn(this)" class="searchSpace" type="text" id="search" name="input_name" placeholder="Search for your dream company..">
        <button class="fancyButton">send</button>
        <label for="search"></label>
    </form>
</template>


<script  type="module" src="../static/js/index.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>""")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
