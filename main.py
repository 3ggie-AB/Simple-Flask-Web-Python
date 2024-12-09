from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/1')
def json():
    return jsonify({"message": "API is working!"})

@app.route('/2')
def html_native():
    return render_template('2.html')

@app.route('/3')
def variabel():
    return render_template('3.html', nama="Egi Ahmad Baihaqi")

@app.route('/4/<user>')
def dynamic_url(user):
    return render_template('3.html', nama=user)

@app.route('/5')
def full_web():
    return render_template('5.html')


if __name__ == '__main__':
    app.run(debug=True)
