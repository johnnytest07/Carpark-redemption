from django.shortcuts import render
from django.http import HttpResponse
from flask import Flask, request, render_template
from .models import TransactionHistory, CouponsTally


# Create your views here.

def home_page(request):
    return render(request, "homepage.html", context={})

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

app = Flask(__name__)

@app.route ('/home/submit', methods=['post'])
def submit(request):
    if request.method == 'POST':
        i1 = request.form['number1']
        i2 = request.form['number2']
        i3 = request.form['number3']    
        i4 = request.form['number4']
        i5 = request.form['number5']
        i6 = request.form['number6']
        i7 = request.form['number7']
    else:
        return render_template('home.html')
#     test = TransactionHistory()
#     test.enter_order(i1, i2, i3, i4, i5, i6, i7)
#     test.payment_method = "hi"
#     test.save()

# # def submitpage(request):
    data = TransactionHistory.objects.all() 
    return render(request, 'transaction_history.html', {'data': data})

