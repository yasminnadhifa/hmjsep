from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def home():
    return render_template('home.html')

@app.route('/kepengurusan',methods=['GET','POST'])
def pengurus():
    return render_template('kepengurusan.html')

@app.route('/kestari',methods=['GET','POST'])
def kestari():
    return render_template('kestari.html')

@app.route('/kaderisasi',methods=['GET','POST'])
def kaderisasi():
    return render_template('kaderisasi.html')


@app.route('/senor',methods=['GET','POST'])
def senor():
    return render_template('senor.html')

@app.route('/latbang',methods=['GET','POST'])
def latbang():
    return render_template('latbang.html')

@app.route('/advokasi',methods=['GET','POST'])
def advokasi():
    return render_template('advokasi.html')

@app.route('/sosmas',methods=['GET','POST'])
def sosmas():
    return render_template('sosmas.html')

@app.route('/danus',methods=['GET','POST'])
def danus():
    return render_template('danus.html')

@app.route('/kominfo',methods=['GET','POST'])
def kominfo():
    return render_template('kominfo.html')

if __name__ == '__main__':
    app.run('0.0.0.0',port=5000,debug=True)