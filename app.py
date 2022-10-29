from flask import Flask, render_template
import requests
app = Flask(__name__)


@app.route('/')
def index():

    datosOptenidos = requests.get('https://api.dailymotion.com/videos?channel=music&limit=20')
    datosformatoJson= datosOptenidos.json()
    


    return render_template('index.html', datos=datosformatoJson['list'])

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 
