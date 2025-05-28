from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<<Hello from a single-file CF app with proper dependencies!>>"

if __name__ == '__main__':
    #app.run(host='0.0.0.0', port=8080)
    app.run()
