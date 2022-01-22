# importing the necessary dependencies
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
# import sklearn
# from sklearn.linear_model import LinearRegression
import pickle

# print (sklearn.__version__)


app = Flask(__name__)  # initializing a flask app


@app.route('/', methods=['GET'])  # route to display the home page
# @cross_origin()
def homePage():
    return render_template("index.html")


@app.route('/predict', methods=['POST', 'GET'])  # route to show the predictions in a web UI
# @cross_origin()
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            crim = float(request.form['crim'])
            zn = float(request.form['zn'])
            indus = float(request.form['indus'])
            chas = float(request.form['chas'])
            nox = float(request.form['nox'])
            rm = float(request.form['rm'])
            age = float(request.form['age'])
            dis = float(request.form['dis'])
            tax = float(request.form['tax'])
            pt_ratio = float(request.form['pt_ratio'])
            b = float(request.form['b'])
            l_stat = float(request.form['l_stat'])

            filename = 'modelForPredRandForest.sav'
            loaded_model = pickle.load(open(filename, 'rb'))  # loading the model file from the storage
            # predictions using the loaded model file
            prediction = loaded_model.predict([[crim, zn, indus, chas, nox, rm, age, dis, tax, pt_ratio, b, l_stat]])
            print('prediction is', prediction)
            # showing the prediction results in a UI
            return render_template('results.html', prediction=prediction[0])
        except Exception as e:
            print('The Exception message is: ', e)
            return 'something is wrong'
    # return render_template('results.html')
    else:
        return render_template('index.html')


# if __name__ == "__main__":
#     #app.run(host='127.0.0.1', port=8001, debug=True)
# 	app.run(debug=True) # running the app
if __name__ == '__main__':
    app.run(debug=True)
