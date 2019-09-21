from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from account.forms import RegistrationForm, AccountAuthenticationForm, AccountUpdateForm
from teller.models import TellerPost

# Create your views here.
def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            room_number = form.cleaned_data.get('room_number')
            phone_number = form.cleaned_data.get('phone_number')
            account = authenticate(email=email, password=raw_password, first_name=first_name, last_name=last_name, phone_number=phone_number, room_number=room_number)
            login(request, account)
            return redirect('login')
        else:
            context['registration_form'] = form

    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'account/register.html', context)

def logout_view(request):
    logout(request)
    return redirect('home')

def login_view(request):

    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect("home")

    if request.POST: 
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect("dashboard")

    else:
        form = AccountAuthenticationForm()

    context['login_form'] = form
    return render(request, 'account/login.html', context)




def account_view(request):

  
     
    if not request.user.is_authenticated:
        return redirect("login")
    
    context = {}

       
    if request.POST:
        form = AccountUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.initial = {
                    "email": request.user.email,
                    "username": request.user.username,
                    "room_number": request.user.room_number,

            }
            form.save()
            context['success_message'] = "Updated"

    else:
        form = AccountUpdateForm(
                initial = {
                    "email": request.user.email,
                    "username": request.user.username,
                    "room_number": request.user.room_number,
                }
            )
    context['account_form'] = form

    teller_posts = TellerPost.objects.filter(author=request.user)
    context['teller_posts'] = teller_posts

    return render(request, 'account/account.html', context)


def gallery_view(request):        
    return render(request, 'account/gallery.html', {})

    
def dashboard_view(request):
    if not request.user.is_authenticated:
        return redirect("login")
    
    return render(request, 'account/dashboard.html', {})

def makepayment_view(request):
    if not request.user.is_authenticated:
        return redirect("login")
        
    return render(request, 'account/make_payment.html', {})
