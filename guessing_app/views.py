from django.shortcuts import render, redirect
import random # import the random module

# Create your views here.
def index(request):
    if 'number' in request.session:
        number = request.session['number']
        print(number)
    else:
        number = random.randint(1, 100) 		# random number between 1-100
        print(number)
        request.session['number'] = number
        print(number)
    context = {
        'number' : number
    }
    return render(request, "index.html", context)

def guess(request):
    number = request.session['number']
    print(number)
    guess = request.POST['guess']
    print(guess)
    if int(guess) > number:
        context = {
            'alert' : "Too high!"
        }
    elif int(guess) < number:
        context = {
            'alert' : "Too low!"
        }
    else:
        context = {
            'alert' : "you got it!"
        }

    return render(request, "index.html", context)





