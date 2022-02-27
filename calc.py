
import requests
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

def mdata():
    response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
    data = response.json()
    return data

values = []


@app.route('/', methods=['GET', 'POST'])
def calc():
    if request.method == 'GET':
        print("We received GET")
        print("We're looking for calc.html page!!!!!")
        data = mdata()
        tradingdate = data[0]['tradingDate']
        rates_len = len(data[0]['rates'])
        rates = data[0]['rates']
        print(rates)
        codes = []
        for i in range(rates_len):
            codes.append(rates[i]['currency'])
        print(codes)
        return render_template("calc.html", tradingdate=tradingdate, codes=codes)
    elif request.method == 'POST':
        print("We received POST")
        values.clear()
        values.append(request.form['mcodes'])
        values.append(request.form['howmany'])
        print(f"We received (values[0]): {values[0]} !!!!")
        print(f"We received (values[1]): {values[1]} !!!!")
        return redirect("/mresult")



@app.route('/mresult', methods=['GET', 'POST'])
def mresult():
    if request.method == 'GET':
        print("We received GET")
        print("We're looking for mresult.html page!!!!!")
        data = mdata()
        tradingdate = data[0]['tradingDate']
        print(f"mcode - {values[0]}")
        mcode = values[0]
        print(f"howmany - {values[1]}")
        howmany = values[1]
        rates = data[0]['rates']
        rates_len = len(data[0]['rates'])
        codes = []
        for i in range(rates_len):
            codes.append(rates[i]['currency'])
        mindex = codes.index(mcode)
        print(mindex)
        mask = rates[mindex]['ask']
        print(mask)
        
        number = float(howmany) * mask

        return render_template("mresult.html", tradingdate=tradingdate, mcode=mcode, howmany=howmany, mask=mask, number=number)
    elif request.method == 'POST':
        return redirect("/")

    



