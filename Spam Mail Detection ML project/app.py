from flask import Flask, request, render_template
from Spam_Mail import spam_prediction
app=Flask(__name__)
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/result',methods=['post','get'])
def resulter():
    content = str(request.form['content'])
    lisg=[]
    lisg.append(content)
    p=spam_prediction(lisg)
    return render_template("result.html",content=lisg,p=p)


if __name__=='__main__':
    app.run(debug=True)