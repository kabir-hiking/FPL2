from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime
from home.models import *
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


import pickle
from django.shortcuts import render
from .forms import DataForm

# Create your views here. :(

def index(request):
   return render (request,"index.html")

def AboutUS(request):
   return render (request,"AboutUS.html")

def ContactUS(request):
   if request.method == "POST":
      name = request.POST.get('name')
      email = request.POST.get('email')
      subject = request.POST.get('subject')
      message = request.POST.get('message')
      ContactUS = Contact(name=name, email=email,subject=subject,message = message,date = datetime.today())
      ContactUS.save()
      messages.success(request,'Your message has been sent! Thank you.')
   return render(request,"ContactUS.html")






def Player(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request,username=username,password=pass1)

        if user is not None:
            login(request,user)
            
            return redirect('MyProfile')
        
        else:
            messages.warning(request, 'Username or Password is incorrect')
            return redirect('Player')
      

        
    return render(request, "Player.html")

def LogoutPage(request):
   logout (request)
   return redirect('Player')

def PlayerReg(request):
   if request.method == "POST":
        uname = request.POST.get('uname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        
        if pass1!= pass2:
            messages.warning(request, "Both passwords didn't match, please try again!")
        else:
            my_user = User.objects.create_user(uname,email,pass1)
            my_user.save ()
            return redirect('Player')
   return render(request, "PlayerReg.html")


def MyHomePage(request):
   return render (request,"MyHomePage.html")

def Prediction(request):
   return render (request,"Prediction.html")




def TermsOfService(request):
   return render (request,"TermsOfService.html")



@login_required(login_url='Player')

def MyProfile(request):
   user = request.user
   context = {
               "uname": user.username,
               "email" : user.email,
            }
   return render (request,"MyProfile.html",context)

def ChangePass(request):
   return render (request,"ChangePass.html")




# predict 


def predict(request):
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            feature1 = form.cleaned_data['feature1']
            # feature2 = form.cleaned_data['feature2']
            # Load the saved model
            model = pickle.load(open('modelNamne.pkl', 'rb'))
            # Make predictions
            prediction = model.predict([feature1])
            return render(request, 'predict.html', {'prediction': prediction})
    else:
        form = DataForm()
    return render(request, 'form.html', {'form': form})

















