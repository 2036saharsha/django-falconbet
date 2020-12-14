from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse 
from django.contrib.auth.models import User, auth
from .models import raila
from .models import adminbet
from django.db import connection
from decimal import Decimal

# Create your views here.




def hi(request):  
    if request.user.is_authenticated:
        author=request.user 
        final= raila.objects.get(author=author)
        return render(request,'thugs/index.html',{"data":final})
    else:
        return render(request,'thugs/index.html')

def register(request):
    author = str(request.user)
    

    if request.method == 'POST':

        password=request.POST['password']
        username=request.POST['username']
        user = User.objects.create_user(username=username,password=password)
        user.save()
        print('user created')
        return redirect('/')
    else:
        return render(request,'thugs/register.html')


def login(request):
    if request.method == 'POST':
        password=request.POST['password']
        username=request.POST['username']
        user = auth.authenticate(username=username,password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('/')

        else:
            messages.info(request,'INVALID CREDENTIALS')
            return redirect('/login')
    else:
        return render(request,'thugs/login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def table(request):
    author=request.user 
    final= raila.objects.get(author=author)
    return render(request,'thugs/table.html',{"data":final})

def data(request):

    if request.method == 'POST':
        bet = request.POST.get('bet', False) #double value details
        if bet == False  and request.POST['betrs']=='':
            messages.info(request,'Enter All Details')
            return redirect('/data')
        elif request.POST['betrs']=='':
            messages.info(request,'Enter Your Amount')
            return redirect('/data')
        elif bet == False:
            messages.info(request,'CHOOSE A CLUB')
            return redirect('/data')
        
        
        else:
            store = adminbet.objects.get(pk=1)
            bet=request.POST['bet']
            betrs=request.POST['betrs']
            print(type(betrs))

            if not int(betrs) > (store.lrange-1):
                messages.info(request,'Low Betting Range')
                return redirect('/data')

            if not int(betrs) < (store.uprange+1):
                messages.info(request,'High Betting Range')
                return redirect('/data')
                                
                                
            if int(betrs)<0:
                messages.info(request,'Negative Balance')
                return redirect('/data')

            author=request.user         # save current username to author
            #Raila=raila(bet=bet,betrs=betrs,author=author) # new user entry
            #Raila.save()
            downtown_store = raila.objects.get(author=author)    

            betrupee= int(betrs)
            coins=downtown_store.coi
            downtown_store.coi = coins-betrupee      #calculating balance
            commision = float(downtown_store.commision)
            a=float(betrupee)
            if request.POST['bet'] == store.club1:
                b=float(store.odds1)
                total1=(a*b) - (commision*a*b)
                total2 = Decimal(total1)
                total3 = round(total2,2)
                total= Decimal(total3)
            elif request.POST['bet'] == store.club2:
                b=float(store.odds2)
                total1=(a*b) - (commision*a*b)
                total2 = Decimal(total1)
                total3 = round(total2,2)
                total= Decimal(total3)




        if downtown_store.coi < 0:  #checking balance
            messages.info(request,'Insufficient Balance')
            return redirect('/data')
        else:
            downtown_store.bet = bet
            downtown_store.betrs = betrupee
            downtown_store.comment = total

            downtown_store.save()
            return redirect('/')

    else:
        store = adminbet.objects.get(pk=1) 
        return render(request,'thugs/data.html',{"data":store})

    