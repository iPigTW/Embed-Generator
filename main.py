from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    name = request.args.get('name')
    description = request.args.get('description')
    color = request.args.get('color')
    image = request.args.get('image')
    return render_template('index.html', name=name, description=description, color=color, image=image)

app.run(port=8080)