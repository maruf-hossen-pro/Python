from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('add.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    num1 = request.form['num1']
    num2 = request.form['num2']
    
    try:
        total = int(num1) + int(num2)
    except ValueError:
        return "Please enter valid numbers."
    
    return render_template('result.html', total=total)

if __name__ == '__main__':
    app.run(debug=True)
