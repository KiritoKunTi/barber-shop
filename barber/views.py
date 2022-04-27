from django.shortcuts import render, redirect
from .models import *
from .forms import BookingForm, ResumeForm, CommentForm, CreatUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView


# Create your views here.
class CustomLoginView(LoginView):
    template_name = 'barber/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('main')
    
    
def logoutUser(request):
    logout(request)
    return redirect('login')
    
    
class RegisterPage(FormView):
    template_name = 'barber/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('main')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
            
        return super(RegisterPage, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('main')    
        return super(RegisterPage, self).get(*args, **kwargs)

# def registerPage(request):
#     if request.user.is_authenticed:
#         return redirect('main')
#     else:
#         if request.method == 'POST':
#             form = CreatUserForm(request.POST)
#             if form.is_valid():
#                 form.save()
#                 return redirect('login')
            
#         else:
#             form = CreatUserForm()
        
#         context = {'form': form}
#         return render(request, 'barber/register.html', context)

@login_required(login_url='login')
def booking(request):

    # create a variable to keep track of the form
    messageSent = False

    # check if form has been submitted
    if request.method == 'POST':

        form = BookingForm(request.POST)

        # check if data from the form is clean
        if form.is_valid():
            cd = form.cleaned_data
            subject = "The BARBERS"
            message = cd['first_name'] + ' ' + cd['last_name'] + ', Thank you for your inquiry about our booking service. We are currently providing top-rated service. In order to provide you an estimation of the cost of our services and more information, our manager will call you.'

            # send the email to the recipent
            send_mail(subject, message,
                      settings.DEFAULT_FROM_EMAIL, [cd['recipient']])

            # set the variable initially created to True
            messageSent = True
            messages.success(request, 'Message was send.')
            return redirect('main')

    else:
        form = BookingForm()
        messages.error(request, 'Something went wrong!!')

    return render(request, 'barber/booking.html', {

        'form': form,
        'messageSent': messageSent,

    })

@login_required(login_url='login')
def main(request):
    return render(request, 'barber/main.html')

@login_required(login_url='login')
def services(request):
    services = Services.objects.all()
    context = {'services': services}
    return render(request, 'barber/services.html', context)

@login_required(login_url='login')
def faq(request):
    faqs = FAQ.objects.all()
    context = {'faqs': faqs}
    return render(request, 'barber/faq.html', context)

@login_required(login_url='login')
def join(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = ResumeForm()
    
    return render(request, 'barber/join_our_team.html', {'form': form})

@login_required(login_url='login')
def team(request):
    barbers = Barbers.objects.all()
    return render(request, 'barber/our_team.html', {'barbers': barbers})

@login_required(login_url='login')
def about(request):
    comments = Comments.objects.all()
    context = {'comments': comments}
    return render(request, 'barber/about.html', context)

@login_required(login_url='login')
def addComment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('about')
    else:
        form = CommentForm()
        
    context = {'form': form}
    return render(request, 'barber/add_comment.html', context)