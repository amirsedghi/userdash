from django.shortcuts import render, redirect
from . import models
from .models import User, Message, Comment
import bcrypt
# Create your views here.
def index(request):
    request.session['id'] = 0
    return render(request, 'userdash/index.html')


def signin(request):
    request.session['id'] = 0
    return render(request, 'userdash/signin.html')


def login(request):
    user = User.objects.filter(email = request.POST['email'])
    password = request.POST['password']
    if bcrypt.hashpw(password.encode('utf-8'), user[0].password.encode('utf-8')) == user[0].password:
        request.session['id'] = user[0].id
        return redirect('/users/show/'+str(user[0].id))
    else:
        return render(request, 'userdash/notfound.html')


def signup(request):
    return render(request, 'userdash/signup.html')

def register(request):
    if request.POST['password'] == request.POST['password_confirm']:
        pw_hash = bcrypt.hashpw(request.POST['password'].encode('utf-8'), bcrypt.gensalt())
        User.objects.create(email = request.POST['email'], first_name = request.POST['first_name'], last_name = request.POST['last_name'], password = pw_hash)
        the_user = User.objects.filter(email = request.POST['email'])
        request.session['id'] = the_user[0].id
        return redirect('/users/show/'+str(the_user[0].id))
    else:
        return render(request, 'userdash/failed.html')


def show(request, id):
    user = User.objects.filter(id = id)
    messages = Message.objects.filter(user_id__id = id)
    comments = Comment.objects.all()
    context = {'messages' : messages, 'user': user[0], 'comments': comments, 'loggedinuser': request.session['id'] }
    return render(request, 'userdash/show.html', context)


def submitMessage(request):
    user = User.objects.filter(id = request.POST['userid'])
    visitor = User.objects.filter(id = request.session['id'])
    Message.objects.create(content = request.POST['message'], user_id = user[0], visitor_id = visitor[0])
    return redirect('/users/show/'+str(user[0].id))

def postComment(request):
    visitor = User.objects.filter(id = request.session['id'])
    message = Message.objects.filter(id = request.POST['message_id'])
    Comment.objects.create(content = request.POST['content'], message_id = message[0], user_id = visitor[0])
    return redirect('/users/show/'+str(request.POST['user_id']))

def dashboard(request):
    user = User.objects.filter(id = request.session['id'])
    allusers = User.objects.all()
    context = {'user': allusers}
    if request.session['id'] == 6 or user[0].admin == 'admin':
        return redirect('/dashboard/admin')
    else:
        return render(request, 'userdash/dashboard.html', context)

def adminDash(request):
    user = User.objects.filter(id = request.session['id'])
    allusers = User.objects.all()
    context = {'user': allusers}
    if request.session['id'] == 6 or user[0].admin == 'admin':
        return render(request, 'userdash/admindash.html', context)
    else:
        return render(request, 'userdash/denied.html')


def edit(request, id):
    user = User.objects.filter(id = id)
    context = {'user': user[0]}
    return render(request, 'userdash/edit.html', context)

def remove(request, id):
    User.objects.filter(id = id).delete()
    return redirect('/dashboard')

def new(request):
    return render(request, 'userdash/new.html')

def create(request):
    if request.POST['password'] == request.POST['password_confirm']:
        pw_hash = bcrypt.hashpw(request.POST['password'].encode('utf-8'), bcrypt.gensalt())
        User.objects.create(email = request.POST['email'], first_name = request.POST['first_name'], last_name = request.POST['last_name'], password = pw_hash)
        return redirect('/dashboard')
    else:
        return render(request, 'userdash/failed.html')

def update(request):
    User.objects.filter(email = request.POST['email']).update(email = request.POST['email'], first_name = request.POST['first_name'], last_name = request.POST['last_name'], admin = request.POST['level'])
    return redirect('/dashboard')

def changePass(request):
    if request.POST['password'] == request.POST['password_confirm']:
        pw_hash = bcrypt.hashpw(request.POST['password'], bcrypt.gensalt())
        User.objects.filter(id = request.POST['id']).update(password = pw_hash)
        return redirect('/dashboard')
    else:
        return render(request, 'userdash/failed.html')

def profile(request):
    user = User.objects.filter(id = request.session['id'])
    context = {'user': user[0]}
    return render(request, 'userdash/edituser.html', context)

def description(request):
    User.objects.filter(id = request.session['id']).update(description = request.POST['description'])
    return redirect('/dashboard')
