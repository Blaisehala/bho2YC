from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages 

# Create your views here.




def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            messages.success(request, f'Account created for {username}!')
            return redirect ('bho-home')

    else:
        form = UserCreationForm()
    return render(request, 'bho/about.html', {'form': form})
    context_instance=RequestContext(request)
   

 

def login(request):
    return render (request, 'users/login.html', {'title':'login'})






