from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from . forms import RegisterForm
from django.contrib import messages
import joblib

# Load the model and vectorizer
model = joblib.load('fake_news_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('predict')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')

def user_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Registration successful!')
            return redirect('login')
        else:
            messages.error(request, "An error occured during the registeration")
    else:
        form = RegisterForm()
        
    return render(request, 'register.html', {'form':form })
        
    
    
    
@login_required
def predict(request):
    if request.method == 'POST':
        text = request.POST['text']
        features = vectorizer.transform([text])
        prediction = model.predict(features)
        result = 'Fake' if prediction[0] == 'fake' else 'Real'
        return render(request, 'predict.html', {'result': result, 'text': text})
    return render(request, 'predict.html')

def home(request):
    return render(request, 'fake_news.html')
