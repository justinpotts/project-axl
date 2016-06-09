import gen_ext
from flask import Flask, send_file, redirect

app = Flask(__name__)

@app.route('/')
def index():
    ext_name = gen_ext.generate()
    return send_file(ext_name + '.xpi', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
