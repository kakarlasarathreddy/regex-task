from flask import Flask, render_template,request,redirect

import re

app = Flask(__name__)

@app.route('/')
def homelook():
    return render_template('home.html')

@app.route('/match', methods = ['GET','POST'])
def matchtext():
    if request.method == 'POST':
            Pattern = request.form['pattern']
            text = request.form['text']
            matches = re.findall(Pattern,text)
            return render_template('regex.html',
                                Pattern = Pattern,
                                text = text,
                                matches = matches
                               )
    return redirect('/')

@app.route('/email',methods=['GET','POST'])
def email_validation():
        if request.method == 'POST':
            email = request.form.get('email')
            error = None 
            match = None
            if re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",email):
                match = "Email is valid" + " " + email
            else:
                error = " This Email Is Not Valid "
            return render_template('email.html',error=error,email=email,match=match)
        return redirect('/')        


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=5000)