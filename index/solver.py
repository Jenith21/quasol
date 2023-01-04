from flask import Flask, request, render_template
import cmath

app = Flask(__name__)

@app.route('/')
def quadratic_solver():
    return render_template('quadratic_form.html')

@app.route('/solve', methods=['POST'])
def solve():
    a = int(request.form['a'])
    b = int(request.form['b'])
    c = int(request.form['c'])
    d = (b**2) - (4*a*c)
    sol1 = (-b-cmath.sqrt(d))/(2*a)
    sol2 = (-b+cmath.sqrt(d))/(2*a)
    return render_template('quadratic_solutions.html', a=a, b=b, c=c, sol1=sol1, sol2=sol2)

if __name__ == '__main__':
    app.run()
