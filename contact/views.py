from django.shortcuts import render, get_object_or_404, redirect
from contact.forms import ContactForm
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

# Create your views here.
def contact_view(request):
    context = {}
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name'] 
            email = form.cleaned_data['email'] 
            comment = form.cleaned_data['comment']

            try:
                full = email + " " + comment
                send_mail(
                    name,
                    email,
                    full,
                    ['shopeyinwale@gmail.com']
                )
                full = email + " " + comment
                context["success_message"] = 'Successfully sent, You will receive a response ASAP'
                form = ContactForm()

            except BadHeaderError:
                return HttpResponse("Invalid")
        
    return render(request, 'contact/contact.html', context)

    