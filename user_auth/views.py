from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def register(request):
    if request.method == 'POST':
        fname = request.POST['f_name']
        lname = request.POST['l_name']
        uname = request.POST['uname']
        email = request.POST['email']
        pasw = request.POST['pasw']

        try:
            user = User.objects.get(username=uname)
            return render(request,'register.html',{'error':True})
        except:
            u=User.objects.create_user(
                first_name = fname,
                last_name = lname,
                email = email,
                username = uname,
                password = pasw,
            )       
        # u.set_password(pasw)
        # u.save()      
    return render(request,'register.html')


def login_(request):
    if request.method =='POST':
        uname = request.POST['uname']
        pasw = request.POST['pasw']
        user = authenticate(request,username=uname,password=pasw)
        print(bool(user))
        if user:
            login(request,user)
            messages.success(request,'login successfully...!')
            return redirect('home')
        else:
            messages.error(request,'entered userame or passowrd is invaild')
            return redirect('login_')
    return render(request,'login_.html')    

@login_required(login_url='login_')
def logout_(request):
    logout(request)
    messages.success(request,'Logout successfully')
    return redirect('login_')         

@login_required(login_url='login_')
def profile(request):
    context ={
        'user':request.user
    }
    return render(request,'profile.html',context)

@login_required(login_url='login_')
def update_profile(request):

    if request.method == "POST":
        try:
            request.user.first_name = request.POST["fname"]
            request.user.last_name = request.POST["lname"]
            request.user.username = request.POST["uname"]
            request.user.email = request.POST["email"]

            request.user.save()

            messages.success(request, "Profile Updated Successfully")
            return redirect("profile")

        except:
            messages.error(request, "Username already exists!")
            return redirect("update_profile")

    return render(request, "update_profile.html")

def reset_pasw(request):
    if request.method == 'POST':
        old_pasw = request.POST['old_pasw']
        user = authenticate(request,username=request.user, password=old_pasw)

        if user:
            messages.success(request, 'Enter new password..!')
            # return redirect('reset_pasw')
            return render(request, 'reset_pasw.html', {'new': True})

        else:
            messages.error(request, 'enterd old password is wrong..!')
            return redirect('reset_pasw')
        
    if 'new_pasw' in request.POST:
        new_pasw = request.POST['new_pasw']
        con_pasw = request.POST['con_pasw']
        if new_pasw != con_pasw:
            messages.error(request,'new password and confirm password are not matching')
            return redirect('reset_pasw')
        if a.check_password(new_pasw):
            messages.error(request,'entered new passwor already exit ')
            return redirect('reset_pasw')
        a = User.objects.get(username = request.user)
        a.set_password(new_pasw)
        a.save()
        messages.success(request,'password is set successfully ')
        return redirect('login_')
    # if con_pasw in request.POST:
    return render(request, 'reset_pasw.html')
def forget_pasw(request):
    if request.method == "POST":
        # First step - check username
        if "uname" in request.POST:
            uname = request.POST["uname"]
            try:
                user = User.objects.get(username=uname)
                request.session["fp_user"] = user.username
                messages.success(request, "Enter new password")
                return render(request, "forget_pasw.html", {"new": True})
            except:
                messages.error(request, "Username doesn't exist")
                return redirect("forget_pasw")
        # Second step - change password
        else:
            new_pasw = request.POST["new_pasw"]
            confirm_pasw = request.POST["confirm_pasw"]
            if new_pasw == confirm_pasw:
                user = User.objects.get(username=request.session["fp_user"])
                user.set_password(new_pasw)
                user.save()
                del request.session["fp_user"]
                messages.success(request, "Password changed successfully")
                return redirect("login_")
            else:
                messages.error(request, "Passwords do not match")
                return render(request, "forget_pasw.html", {"new": True})

    return render(request, "forget_pasw.html")