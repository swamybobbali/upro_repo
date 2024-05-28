from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
# Create your views here.
def home(request):
    return render(request,'testapp/home.html')
def latest(request):
    return render(request, 'testapp/latest.html')
@login_required
def toly(request):
    return render(request, 'testapp/toly.html')
@login_required
def boly(request):
    return render(request, 'testapp/boly.html')
@login_required
def holy(request):
    return render(request,'testapp/holy.html')
def logout(request):
    return render(request,'testapp/logout.html')
from testapp.forms import SignupFrom
def signup(request):
    form=SignupFrom()
    if request.method== 'POST':
        form=SignupFrom(request.POST)
        #form.save()
        user=form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'testapp/signup.html',{'form':form})