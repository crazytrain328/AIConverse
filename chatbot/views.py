from django.shortcuts import render,redirect
from django.http import JsonResponse
import openai
from openai import OpenAI
from django.contrib import auth
from django.contrib.auth.models import User
from .models import Chat
from django.utils import timezone
from django.contrib.auth.decorators import login_required
# Create your views here.

openai_api_key=''
openai.api_key= openai_api_key

def ask_openai(message,api_key):
    client = OpenAI()
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": message}
    ]
    )
    print(response)
    response = response['choices'][0]['message']['content']
    return response

@login_required(login_url="login")
def home(request):
    chats= Chat.objects.filter(user= request.user)
    if request.method == 'POST':
        message = request.POST.get('message')
        response= ask_openai(message)
        chat= Chat(user=user.username, message=message, response=response, created_at= timezone.now())
        chat.save()
        return JsonResponse({'message':message, 'response': response})

    return render(request, 'chatbot.html',{'chats':chats})

def login(request):
    print("Beginning of the method")
    if request.method == 'POST':
        print("request method post")
        try:
            username = request.POST['username']
            password= request.POST['password']
            user= auth.authenticate(request,username=username,password=password)
            if user is not None: 
                auth.login(request, user)
                return redirect('home')
            else:
                error_message='Wrong Credentials'
                return render(request, 'login.html', {'error_message':error_message})
        except:
            error_message='Error Logging In'
            return render(request, 'login.html', {'error_message':error_message})

    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 == password2:
            try:
                user= User.objects.create_user(username,email,password1)
                print("here")
                
                user.save()
                
                print("User Saved")
                auth.login(request=request, user=user)
                print("User Logged In")
                return redirect('')
            except Exception as e:
                print(e)
                error_message='Error Creating Account'
                return render(request, 'register.html', {'error_message':error_message})
        else:
            error_message= 'Password Do Not Match'
            return render(request, 'register.html', {'error_message':error_message})

    return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('login')

def clear_chat(request):
    chat = Chat.objects.filter(user= request.user)
    chat.delete()
    return render(request, 'chatbot.html')