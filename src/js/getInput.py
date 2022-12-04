from flask import Flask, request, render_template

app = Flask(__name__, template_folder="../src")


@app.route('/')
def render():
    return render_template("index.html")


# @app.route('/#welcome', methods=['GET'])
# def input_data() -> str:
#     data = request.input_stream['input_name']
#     return str(data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
