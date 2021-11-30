from flask import Flask, request, jsonify, render_template, url_for, redirect
from csv import writer
import pandas as pd
import numpy as np
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'dr_shridevi@rediffmail.com' or request.form['password'] != 'heroku':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home_page'))
    return render_template('login.html', error=error)

@app.route('/home')
def home_page():
    return render_template("index.html")

@app.route('/patient_logs')
def log_book():
    return render_template("forms-elements.html")

@app.route('/patient_logs',methods=['POST'])
def appending():

    P_Id = request.form['P_Id']
    Name = request.form['Name'].upper()
    Age = request.form['Age']
    Sex = request.form.get('Sex').upper()
    Phone_Number = request.form['Phone_Number']
    Locality = request.form['Locality'].upper()
    Date = request.form['Date']
    Link = request.form['Link']
    l1=[P_Id,Name,Age,Sex,Phone_Number,Locality,Date,Link]
    # write_log(l1)
    with open("Pt_log.csv", 'a') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(l1)
        f_object.close()
    output="Patient Logged"
    return render_template('forms-elements.html', prediction_text='{}'.format(output))

@app.route('/query')
def query_page():
    return render_template('query.html')

# @app.route('/query',methods=['POST'])
# def querying():

    # Phone_Number = request.form['Phone_Number']
    # df = pd.read_csv("Pt_log.csv")
    # temp = df.loc[df['Phone_Number']==Phone_Number]
    # fPID=list(temp["P_Id"])
    # fPID=fPID[0]
    # fName=list(temp["Name"])
    # fName = fName[0]
    # fDate=list(temp["Date"])
    # fDate = fDate[0]
    # fLink=list(temp["Link"])
    # fLink = fLink[0]
    # return render_template('query.html', jPID='{}'.format(fPID))
@app.route('/query',methods=['POST'])
def query1():

    Phone_Number = request.form['Phone_Number']
    Phone_Number=int(Phone_Number)
    df = pd.read_csv("Pt_log.csv")
    res = df.loc[df['Phone_Number'] == Phone_Number]
    name=list(res['Name'])
    fPID=list(res['P_Id'])
    link=list(res['Link'])
    fDate=list(res['Date'])
    answer = []
    for y in range(len(name)):
        a = name[y]
        b = fDate[y]
        c = link[y]
        temp = [a, b, c]
        answer.append(temp)
    l=len(answer)

    #     return render_template('query.html', prediction_text='{}'.format(x))
    # return render_template('query.html',l = len(res), res = res)
    return render_template('query.html', prediction_text='{}'.format(name),jPID='{}'.format(fPID),jDate='{}'.format(fDate),jLink='{}'.format(link),queriedres='{}'.format(answer))


if __name__ == '__main__':
    app.run(debug=True)