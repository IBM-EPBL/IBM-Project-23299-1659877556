from flask import Flask, render_template, request
import pickle



app = Flask(__name__)

model = pickle.load(open(r'C:\Users\kotha\OneDrive\Desktop\Loan prediction Ml model\rdf.pkl','rb'))

@app.route('/')
def Home():
    return render_template('home.html')

@app.route('/predict.html')


@app.route('/predict',methods = ['POST','GET'])
def predict():
    if request.method == "POST":
        gender = request.form['genderBox']
        married = request.form['maritalBox']
        dependents = request.form['dependents']
        education = request.form['educationBox']
        employment = request.form['employmentBackground']
        applicant_income = request.form['applicantIncomeBox']
        coapplicant_income = request.form['coApplicantIncomeBox']
        loan_amount = request.form['laonAmtBox']
        loan_amount_term = request.form['laonAmtTermBox']
        credit_history = request.form['CHBox']
        prop_area = request.form['propertyAreaBox']

        if gender == 'Male':
            gender = 1
        else:
            gender = 0

        if married == 'Yes':
            married = 1
        else:
            married = 0

        if dependents == '0':
            dependents = 0
        elif dependents == '1':
            dependents = 1
        elif dependents == '2':
            dependents = 2
        else:
            dependents = 3

        if education == 'Graduate':
            education = 0
        else:
            education = 1

        if employment == 'Yes':
            employment = 1
        else:
            employment = 0
        if credit_history=='Yes':
            credit_history=1
        else:
            credit_history=0
        if prop_area == 'Rural':
            prop_area = 0
        elif prop_area == 'Semiurban':
            prop_area = 1
        else:
            prop_area = 2
        prediction=model.predict([[gender,married,dependents, education, employment,applicant_income,coapplicant_income,loan_amount, loan_amount_term,credit_history,prop_area]])
        if(prediction=="N"):
            prediction="No"
        else:
            prediction="Yes"
            return render_template("predict.html", prediction_text="Congratulations your loan status is {}".format(prediction))
    else:
          return render_template("predict.html")


if __name__ == "__main__":
    app.run(debug=True)