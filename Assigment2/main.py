from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('form.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.upper()
    l1=list(processed_text)
    l2=['A','E',"I","O","U"]
    cnt=0
    for i in l1:
        if i in l2:
            cnt=cnt+1
    r="{:.2f}".format(cnt/len(l1))
    return r
if __name__ == '__main__':
    app.run(debug=True)
