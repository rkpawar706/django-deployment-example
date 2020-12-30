from django.shortcuts import render
from.forms import Userform,Usermodelform


#these are the imports for the login and logout

from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth import authenticate






# Create your views here.
def index(request):
    return render(request,"index.html",context={'f':1})

def register(request):
    Registered = False
    if request.method == 'POST':
        form1 = Userform(data=request.POST)
        form2 = Usermodelform(data=request.POST)
        if form1.is_valid() and form2.is_valid():
            Registered = True
            user1 = form1.save()
            user1.set_password(user1.password)
            user1.save()
            #this method is used when there is password in your data if this was a normal form .save and the
            #commit = true would have done the work
            #this is the new name and is diffrent from the one defined earlier
            profile = form2.save(commit=False)
            profile.user = user1

            if"profile_image" in request.FILES:
                profile.profile_image = request.FILES['profile_image']

            profile.save()

            #pahle user jo upar keyword liya tha uska part overwrite kar do
            #phir agar koi bhi pdf csv aur koi file type h to use aise alag se add karo agar form ke kisi bhi instance ko save karoge vo apne app save ho jayega







    else:
        form1=Userform()
        form2=Usermodelform()


    my_dict ={"f1":form1,"f2":form2, "registered":Registered}


    return render(request,"register.html", context=my_dict)



def u_login(request):
    if request.method=="POST":
        username1 = request.POST.get('username')
        password1 = request.POST.get('password')
        user = authenticate(username=username1 , password =password1)
        if user:
            if user.is_active:
                login(request,user)

                return HttpResponseRedirect(reverse("index"))
            else:
                return HttpResponse("the account is not active now ")
        else:
            return HttpResponse("INCORRECT USERNAME OR PASSWORD ")



    else:
        return render(request,'login.html')


@login_required
def u_logout(request):
    logout(request)
    return index(request)
