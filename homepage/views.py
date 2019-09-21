from django.shortcuts import render


def home_screen_view(request):
    return render(request, 'home.html', {})

def profile_page_view(request):
    return render(request, 'profilepage.html', {})



