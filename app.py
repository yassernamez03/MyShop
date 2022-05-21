from flask import Flask, redirect , render_template, request, session,url_for
from wtf import Com
app = Flask(__name__)
app.config['SECRET_KEY']='QFVKEBR392RIR2NF2DL'
products = [{
        "id": 1,
        "marque": "DELL",
        "model": "LATITUDE 460",
        "prix": 6800,
        "qtt": 42,
        "img":'1.jpeg',
        "description": "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Porro minima ex, cupiditate doloribus id quae eius odio blanditiis autem in maxime qui doloremque. Ducimus consectetur, eaque suscipit beatae placeat molestiae.",

    },
    {
        "id": 2,
        "marque": "LENOVO",
        "model": "x1 yoga",
        "prix": 7800,
        "qtt": 42,
        "img":'2.jpeg',
        "description": "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Porro minima ex, cupiditate doloribus id quae eius odio blanditiis autem in maxime qui doloremque. Ducimus consectetur, eaque suscipit beatae placeat molestiae.",

    },
    {
        "id": 3,
        "marque": "DELL",
        "model": "LATITUDE 100",
        "prix": 12000,
        "qtt": 42,
        "img":'3.jpeg',
        "description": "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Porro minima ex, cupiditate doloribus id quae eius odio blanditiis autem in maxime qui doloremque. Ducimus consectetur, eaque suscipit beatae placeat molestiae.",

    },
    {
        "id": 4,
        "marque": "LENOVO",
        "model": "X280",
        "prix": 8800,
        "qtt": 42,
        "img":'4.jpeg',
        "description": "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Porro minima ex, cupiditate doloribus id quae eius odio blanditiis autem in maxime qui doloremque. Ducimus consectetur, eaque suscipit beatae placeat molestiae.",

    },
    {
        "id": 5,
        "marque": "DELL",
        "model": "LATITUDE 460",
        "prix": 6800,
        "qtt": 42,
        "img":'5.jpeg',
        "description": "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Porro minima ex, cupiditate doloribus id quae eius odio blanditiis autem in maxime qui doloremque. Ducimus consectetur, eaque suscipit beatae placeat molestiae.",

    }
]
chart = {}
total = 0
infos = {}
@app.route('/add/<int:id>/<int:prix>')
def add(id,prix):
    global total
    if id not in chart:
        chart[id] = products[id-1]
        chart[id]['times'] = 1
    else:
        chart[id]['times'] += 1
    total +=prix
    return redirect(url_for('index'))
@app.route('/')
def index():
    return render_template('index.html',products=products,chart=chart)
@app.route('/pannier')
def pannier():
    return render_template('pannier.html',products=products,chart=chart,total=total)
@app.route('/contact',methods=["POST","GET"])
def contact():
    global infos
    form = Com()
    if form.validate_on_submit():
        email =  form.email.data
        comments = form.text.data
        infos[email] = comments
        return redirect(url_for('contact'))
    return render_template('contact.html',form=form)
@app.route('/del/<int:id>')
def delete(id):
    global total
    if id in chart:
        total-= chart[id]["prix"]
        chart[id]["times"]-=1
    if chart[id]["times"] < 1:
        chart.pop(id)
    return redirect(url_for('pannier'))
@app.route('/comments')
def comments():
    global infos
    return render_template('comments.html',infos=infos)
if __name__=="__main__":
    app.run(debug=True)
