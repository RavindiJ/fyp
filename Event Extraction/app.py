from flask import Flask,render_template,request
from werkzeug.utils import secure_filename
from Report import extractText
from NER import ner

def proccess(fileName):
    list = extractText(fileName)
    for key in list:
        sentences = list.get(key)
        print()
        ner(sentences)

app = Flask(__name__)
@app.route('/form')
def form():
    return render_template('form.html')
 
@app.route('/upload', methods = ['POST', 'GET'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        fileName = secure_filename(f.filename)
        f.save(fileName) 
        proccess(fileName)
        return "File saved successfully"
 
app.run(host='localhost', port=5000, debug=True)
