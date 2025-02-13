# users/views.py
from django.urls import reverse_lazy
from django.views import generic
from .forms import EditProfileForm
from .forms import CustomUserCreationForm
from django.shortcuts import render,redirect
class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def edit_profile(request):
    if request.method=='POST':
        form= EditProfileForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            
            return redirect('home')
    else:
        form=EditProfileForm(instance=request.user)
    context={'form':form}
    return render(request,'edit_profile.html',context)