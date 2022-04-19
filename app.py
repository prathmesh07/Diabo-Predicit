import numpy as np
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
sc = pickle.load(open('sc.pkl', 'rb'))
model = pickle.load(open('classifier.pkl', 'rb'))


@app.route('/')
def hello_world():
    return render_template("index.html")
database={'Prathmesh':'pass@123','Mihir':'pass@123','Jay':'pass@123','Harsh':'pass@123','Sakshi':'pass@123','Ashlesha':'pass@123'}

@app.route('/home')
def heello_world():
    return render_template('ditect.html')



# @app.route('/')
# def home():
#     return render_template('ditect.html')

@app.route('/form_login',methods=['POST','GET'])
def login():
    name1=request.form['username']
    pwd=request.form['password']
    if name1 not in database:
	    return render_template('login.html',info='Invalid User')
    else:
        if database[name1]!=pwd:
            return render_template('login.html',info='Invalid Password')
        else:
	         return render_template('ditect.html',name=name1)


@app.route('/signout')
def helllo_world():
    return render_template("index.html")
database={'Prathmesh':'pass@123','Mihir':'pass@123','Siddharth':'pass@123','Kshitij':'pass@123','Simran':'pass@123','Leela':'pass@123'}



@app.route('/team')
def team():
    return render_template('Team.html')

@app.route('/contact')
def contact():
    return render_template('Contact.html')

@app.route('/Info')
def Info():
    return render_template('Info.html')

@app.route('/predict',methods=['POST'])
def predict():
    
    float_features = [float(x) for x in request.form.values()]
    final_features = [np.array(float_features)]
    pred = model.predict( sc.transform(final_features) )
    return render_template('result.html', prediction = pred)

if __name__ == "__main__":
    app.run(debug=True)
