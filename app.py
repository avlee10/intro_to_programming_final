from flask import Flask, send_file, make_response, render_template, request
import calculator
import csv


# create the application object
app = Flask(__name__)

# use decorators to link the function to a url
@app.route('/')
def home():
    return render_template('input_data.html')

@app.route('/results', methods = ['GET','POST'])
def alcoholcontent():
    if request.method == 'POST':
        result = request.form
        mydata = calculator.A(vodka = int(result['vodka_']),gin = int(result['gin_']),rum = int(result['rum_']),whiskey = int(result['whiskey_']),tequila = int(result['tequila_']),liqeurs = int(result['liqeurs_']),fortwine = int(result['fortwine_']), unfortwine = int(result['unfortwine_']),beer = int(result['beer_']),maltbev = int(result['maltbev_']))
        yourdata = round(calculator.BACP(weight=float(result['weight_']), gender = str(result['gender_']), starttime= float(result['starttime_']), myalc=mydata),2)
        ourdata = round(calculator.TD( tbacp= yourdata),2)
        wedata = calculator.linegraph2(xd= yourdata)
        bytes_object= calculator.display( myy= wedata, bacp=yourdata,F= ourdata)
        return send_file(bytes_object, attachment_filename='plot.png', mimetype='image/png')
        

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug = True)