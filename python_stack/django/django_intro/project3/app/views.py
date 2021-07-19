from django.shortcuts import render, redirect
import random
from datetime import datetime

def fun(request):
    if "Gold" not in request.session or "activities" not in request.session:
        request.session['Gold'] = 0
        request.session['activities'] = []
    return render(request, "index.html")


def process_money(request):
    if request.method == "POST":
        if request.POST['hiddeninput'] == 'farm':
            gold = random.randint(10, 21)
            request.session['activities'].append('You are earned ' + str(gold) + ' golds from the ' +
            request.POST['hiddeninput'] + ' ' + '(' + str(datetime.now().strftime("%Y-%m-%d %H:%M")) + ')')
            

        elif request.POST['hiddeninput'] == 'cave':
            gold = random.randint(5, 11)
            request.session['activities'].append('You are earned ' + str(gold) + ' golds from the ' +
            request.POST['hiddeninput'] + ' ' + '(' + str(datetime.now().strftime("%Y-%m-%d %H:%M")) + ')')

        elif request.POST['hiddeninput'] == 'house':
            gold = random.randint(2, 6)
            request.session['activities'].append('You are earned ' + str(gold) + ' golds from the ' +
            request.POST['hiddeninput'] + ' ' + '(' + str(datetime.now().strftime("%Y-%m-%d %H:%M")) + ')')

        elif request.POST['hiddeninput'] == 'casino':
            gold = random.randint(-50, 51)
            if gold >= 0:
                request.session['activities'].append('Entered a casino and earned ' + str(
                gold) + ' gold' + ' ' + '(' + str(datetime.now().strftime("%Y-%m-%d %H:%M")) + ')')
            else:
                request.session['activities'].append('Entered a casino and lost ' + str(
                gold) + ' gold... Ouch...' + ' ' + '(' + str(datetime.now().strftime("%Y-%m-%d %H:%M")) + ')')

        request.session['Gold'] += gold

        return redirect('/')
def reset(request):
    if request.method == "POST":
        request.session['Gold'] = 0
        request.session['activities'] = []
    return redirect('/') 

