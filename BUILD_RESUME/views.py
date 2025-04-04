from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from datetime import datetime,date
from django.contrib.auth import login,logout,authenticate
from User_App.models import user_data
import base64

def check_superuser(request):
    superuser_exists = User.objects.filter(is_superuser=True).exists()
    
    if superuser_exists:
        return HttpResponse("At least one superuser exists.")
    else:
        return HttpResponse("No superuser exists.")

def home(request):
    return render(request,"index.html")

def sign_up(request):  
    if request.method=="POST":
        user_html=request.POST['u_name']
        pass_html=request.POST['u_pass']
        confirm_pass_html=request.POST['u_ag_pass']
        if not all([user_html, pass_html, confirm_pass_html]):
            error="Empty Fields Please Fill Up !"            
            return render(request,"sign_up.html",{'error':error})
        if User.objects.filter(username=user_html).exists():
            exits = "Username already exists. Please choose a different username."
            return render(request, "sign_up.html", {'error': exits})
        if confirm_pass_html==pass_html:
            new_user=User.objects.create_user(username=user_html,password=pass_html)
            login(request,new_user)
            return redirect("/resume")
        else:
            error="Passwords not match."
            return render(request,"sign_up.html",{'error':error})
    return render(request,"sign_up.html")

def sign_in(request): 
    if request.method=="POST":
        user_html=request.POST['u_name']
        pass_html=request.POST['u_pass']
        user_valid=authenticate(username=user_html,password=pass_html)
        if user_html=="":
            error="Empty Fields Please Fill Up !"            
            return render(request,"sign_in.html",{'error':error})
        if user_valid is not None:
            login(request,user_valid)    
            msg="Welcome to " 
            messages.success(request, msg)  
            request.session['pass'] = pass_html
            return redirect("/resume")
        else:
            error = "Invalid username or password."
            return render(request,"sign_in.html",{'error':error})
    return render(request,"sign_in.html")

def sign_out(request):
    logout(request)
    return render(request,"sign_up.html")

def resume(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            print(request.POST)
            obj=user_data.objects.filter(username=str(request.user)+str(request.session.get('pass',''))).exists()
            if not obj:
                user_data_instance = user_data(
                username=str(request.user)+str(request.session.get('pass','')),

                intro_firstname=request.POST['firstname'],
                intro_middlename=request.POST['middlename'],
                intro_lastname=request.POST['lastname'],

                # intro_image=request.POST['image'],
                intro_image=base64.b64encode(request.FILES.get('image').read()).decode('utf-8'),

                intro_designation=request.POST['designation'],
                intro_address=request.POST['address'],

                intro_email=request.POST['email'],
                intro_phone=request.POST['phoneno'],
                intro_summary=request.POST['summary'],

                achi_title=request.POST.getlist('achieve_title'),
                achi_description=request.POST.getlist('achieve_description'),

                exp_title=request.POST.getlist('exp_title'),
                exp_company=request.POST.getlist('exp_organization'),
                exp_location=request.POST.getlist('exp_location'),
                exp_start_date=request.POST.getlist('exp_start_date'),
                exp_end_date=request.POST.getlist('exp_end_date'),
                exp_description=request.POST.getlist('exp_description'),

                edu_school=request.POST.getlist('edu_school'),
                edu_degree=request.POST.getlist('edu_degree'),
                edu_city=request.POST.getlist('edu_city'),
                edu_start_date=request.POST.getlist('edu_start_date'),
                edu_end_date=request.POST.getlist('edu_graduation_date'),
                edu_description=request.POST.getlist('edu_description'),    

                proj_name=request.POST.getlist('proj_title'),
                proj_link=request.POST.getlist('proj_link'),
                proj_description=request.POST.getlist('proj_description'),

                skills=request.POST.getlist('skill')
                )
                user_data_instance.save()   
            else:
                obj=user_data.objects.filter(username=str(request.user)+str(request.session.get('pass',''))).first()
                # If a record exists, update it
                if request.POST.get('firstname'):
                    obj.intro_firstname = request.POST.get('firstname', '')
                if request.POST.get('middlename'):
                    obj.intro_middlename = request.POST.get('middlename', '')
                if request.POST.get('lastname'):
                    obj.intro_lastname = request.POST.get('lastname', '')
                if request.FILES.get('image'):
                    obj.intro_image=base64.b64encode(request.FILES.get('image').read()).decode('utf-8')
                if request.POST.get('designation'):
                    obj.intro_designation = request.POST.get('designation', '')
                if request.POST.get('address'):
                    obj.intro_address = request.POST.get('address', '')
                if request.POST.get('email'):
                    obj.intro_email = request.POST.get('email', '')
                if request.POST.get('phoneno'):
                    obj.intro_phone = request.POST.get('phoneno', '')
                if request.POST.get('summary'):
                    obj.intro_summary = request.POST.get('summary', '')

                if request.POST.getlist('achieve_title'):
                    obj.achi_title = request.POST.getlist('achieve_title', '')
                if request.POST.getlist('achieve_description'):
                    obj.achi_description = request.POST.getlist('achieve_description', '')

                if request.POST.getlist('exp_title'):
                    obj.exp_title = request.POST.getlist('exp_title', '')
                if request.POST.getlist('exp_organization'):
                    obj.exp_company = request.POST.getlist('exp_organization', '')
                if request.POST.getlist('exp_location'):
                    obj.exp_location = request.POST.getlist('exp_location', '')
                if request.POST.getlist('exp_start_date'):
                    obj.exp_start_date = request.POST.getlist('exp_start_date', date.today())
                if request.POST.getlist('exp_end_date'):
                    obj.exp_end_date = request.POST.getlist('exp_end_date', date.today())
                if request.POST.getlist('exp_description'):
                    obj.exp_description = request.POST.getlist('exp_description', '')

                if request.POST.getlist('edu_school'):
                    obj.edu_school = request.POST.getlist('edu_school', '')
                if request.POST.getlist('edu_degree'):
                    obj.edu_degree = request.POST.getlist('edu_degree', '')
                if request.POST.getlist('edu_city'):
                    obj.edu_city = request.POST.getlist('edu_city', '')
                if request.POST.getlist('edu_start_date'):
                    obj.edu_start_date = request.POST.getlist('edu_start_date', date.today())
                if request.POST.getlist('edu_graduation_date'):
                    obj.edu_end_date = request.POST.getlist('edu_graduation_date', date.today())
                if request.POST.getlist('edu_description'):
                    obj.edu_description = request.POST.getlist('edu_description', '')

                if request.POST.getlist('proj_title'):
                    obj.proj_name = request.POST.getlist('proj_title', '')
                if request.POST.getlist('proj_link'):
                    obj.proj_link = request.POST.getlist('proj_link', '')
                if request.POST.getlist('proj_description'):
                    obj.proj_description = request.POST.getlist('proj_description', '')
                    
                if request.POST.getlist('skill'):
                    obj.skills = request.POST.getlist('skill', '')
                obj.save()
            messages.success(request, "Resume saved successfully!")
            # return render(request, "resume.html")
        # return render(request,"resume.html")
        obj = user_data.objects.filter(username=str(request.user)+str(request.session.get('pass',''))).exists()
        if obj:
            obj=user_data.objects.filter(username=str(request.user)+str(request.session.get('pass',''))).first()
            obj.achi_title = eval(obj.achi_title)
            obj.achi_description = eval(obj.achi_description)

            obj.exp_title = eval(obj.exp_title)
            obj.exp_company = eval(obj.exp_company)
            obj.exp_location = eval(obj.exp_location)
            obj.exp_start_date = obj.exp_start_date
            obj.exp_end_date = obj.exp_end_date
            obj.exp_description = eval(obj.exp_description)

            obj.edu_school = eval(obj.edu_school)
            obj.edu_degree = eval(obj.edu_degree)
            obj.edu_city = eval(obj.edu_city)
            obj.edu_start_date = obj.edu_start_date
            obj.edu_end_date = obj.edu_end_date
            obj.edu_description = eval(obj.edu_description)

            obj.proj_name = eval(obj.proj_name)
            obj.proj_link = eval(obj.proj_link)
            obj.proj_description = eval(obj.proj_description)

            obj.skills = eval(obj.skills)
            return render(request,'resume.html',
            {'obj': obj,
            'achievements':zip(obj.achi_title, obj.achi_description),
            'experiences':zip(obj.exp_title,obj.exp_company,obj.exp_location,obj.exp_start_date,obj.exp_end_date,obj.exp_description),
            'educations':zip(obj.edu_school,obj.edu_degree,obj.edu_city,obj.edu_start_date,obj.edu_end_date,obj.edu_description),
            'projects':zip(obj.proj_name,obj.proj_link,obj.proj_description),
            'skills':obj.skills
            })
        return render(request,'resume.html')
    else:
        return redirect('/sign_in/')