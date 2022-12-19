import pickle
import json
import pandas as pd
import numpy as np
import config1
import sklearn

class SalaryData():
    def __init__(self, YearsExperience):
        self.YearsExperience = YearsExperience

    def load_model(self):
        with open("Linear_Reg_Model.pkl", "rb") as f:
            self.model = pickle.load(f)

    def get_predicted_salary(self):
        self.load_model()

        test_array = np.zeros(1)
        # test_array[0] = eval(self.YearsExperience['YearsExperience'])
        
        test_array[0] = self.YearsExperience

        print("Test Array : \n", test_array)
        predicted_salary = self.model.predict([test_array])[0]  
        print("Predicted_salary :",predicted_salary)
        return np.around(predicted_salary, 2)


if __name__ == "__main__":
    
    salary_data = SalaryData(YearsExperience)
    salary_data

     # print()
    # print(f"Predicted Salary  is {salary}/- Rs. Only")


            