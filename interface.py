from distutils.command.config import config
from flask import Flask, jsonify, render_template, request
import config1
# import models
from utils import SalaryData
import sklearn


app = Flask(__name__)

@app.route('/')
def hello_flask():
    print("Welcome to Employee Salary Prediction")
    return render_template("index.html")

@app.route('/emp_salary', methods = ["POST", "GET"])
def emp_salary():
    if request.method == 'POST':
        print("We are using POST Method")

        YearsExperience = eval(request.form["YearsExperience"])

        print("Years of Experience\n", YearsExperience)

    
        salary_data = SalaryData(YearsExperience)
        salary = salary_data.get_predicted_salary()

        if salary < 0:
            salary = 'Invalid inputs, Please try again.'

        return render_template("index.html", prediction = salary)
        # return jsonify({"Result" : f"Predicted Salary is {salary}/- Rs. "})

    else:
        print("We are using GeT Method")
        YearsExperience = eval(request.form["YearsExperience"])

        print("Years of Experience\n", YearsExperience)

        salary_data = SalaryData(YearsExperience)
        salary = salary_data.get_predicted_salary()

        if salary < 0:
            salary = 'Invalid inputs, Please try again.'

        return render_template("index.html", prediction = salary)
        # return jsonify({"Result" : f"Predicted Salary is {salary}/- Rs. "})
    
    
if __name__ == "__main__":
    app.run(host='0.0.0.0' , port= config1.PORT_NUMBER, debug=True)
