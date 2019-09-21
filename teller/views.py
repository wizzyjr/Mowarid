from django.shortcuts import render, redirect, get_object_or_404

from teller.models import TellerPost
from teller.forms import CreateTellerForm, UpdateTellerPostForm
from account.models import Account

def add_teller_view(request):

    context = {}

    user = request.user
    if not user.is_authenticated:
        return redirect('login')

    form = CreateTellerForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        author = Account.objects.filter(email=user.email).first()
        obj.author = author
        obj.save()
        context['success_message'] = 'Teller uploaded successfully'

        form = CreateTellerForm()

    context['form'] = form
    return render(request, 'teller/add_teller.html', {})

def detail_teller_view(request, slug):

    context = {}
    if not request.user.is_authenticated:
        return redirect("login")
    teller_post = get_object_or_404(TellerPost, slug=slug)
    context['teller_post'] = teller_post
    return render(request, 'teller/detail_teller.html', context)

def edit_teller_view(request, slug):
    
    context = {} 

    user = request.user
    if not user.is_authenticated:
        return redirect("login")

    teller_post = get_object_or_404(TellerPost, slug=slug)
    if teller_post.author != user:
        return HttpResponse("You are not allowed to view this page!!") 

    if request.POST:
        form = UpdateTellerPostForm(request.POST or None, request.FILES or None, instance=teller_post)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            context['success_message'] = 'Updated'
            teller_post = obj

    form = UpdateTellerPostForm(
            initial = {
                    # "title": teller_post.title,
                    "body": teller_post.body,
                    "image": teller_post.image,
            }
    )

    context['form'] = form
    return render(request, 'teller/edit_teller.html', context)
