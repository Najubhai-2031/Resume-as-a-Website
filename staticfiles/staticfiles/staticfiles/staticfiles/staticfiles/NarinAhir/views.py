import email
import imp
import re
from telnetlib import AUTHENTICATION
from click import password_option
from colorama import Cursor
from django.shortcuts import render
import mysql.connector as sql
from loginapp.models import User
from operator import itemgetter
from django.contrib import messages
from django.contrib.auth import login, authenticate
fname=''
lname=''
sex=''
em=''
pwd=''



def home(request):
    return render(request, 'home.html')

def loginnow(request):
    global em,pwd
    if request.method=="POST":
        con = sql.connect(host="localhost", user="root", passwd='20312661999',database="login")
        cursor = con.cursor()
        d = request.POST
        for key, value in d.items():
            if key == "email":
                em = value
            if key == "password":
                pwd = value
        c = "select * from users where email='{}' and password='{}'".format(em, pwd)
        cursor.execute(c)
        t = tuple(cursor.fetchall())
        while True:
                if t == ():
                    messages.info(request,"Please enter the correct username and password. Note that both fields may be case-sensitive.")
                    # return render(request, 'error.html')
                    break
                else:
                    return render(request, 'profile.html')
    return render(request, 'login_page.html')

def signupnow(request):
    global fname, lname, sex, em, pwd
    if request.method == "POST":
        m = sql.connect(host="localhost", user="root", passwd="20312661999", database='login')
        cursor = m.cursor()
        d = request.POST
        for key, value in d.items():
            if key == "First_Name":
                fname = value
            if key == "Last_Name":
                lname = value
            if key == "sex":
                sex = value
            if key == "email":
                em = value
            if key == "password":
                pwd = value

        c = "insert into users Values('{}','{}','{}','{}','{}')".format(fname, lname, sex, em, pwd)
        cursor.execute(c)
        m.commit()
        messages.info(request, "Account Created Succesfully !!!")
    return render(request, 'signup_page.html')

def aboutme(request):
    return render(request, 'aboutme.html')

def profile(request):
    return render(request, 'profile.html')

def user_logout(request):
    # logout(request)
    return render(request, 'home.html')