from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/')
def upload_file():
    return render_template('form.html')


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file_post():
    if request.method == 'POST':
        f = request.files['file']
        #f.save(secure_filename(f.filename))
        f=open(f.filename,"r")
        data=f.read()
        l1 = list(data.upper())
        l2 = ['A', 'E', "I", "O", "U"]
        cnt = 0
        for i in l1:
            if i in l2:
                cnt = cnt + 1
        r = "{:.2f}".format(cnt / len(l1))
        return r


if __name__ == '__main__':
    app.run(debug=True)
