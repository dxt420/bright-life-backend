from django.shortcuts import render,reverse,redirect,get_object_or_404
from django.http import HttpResponseRedirect
from . models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.



def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    messages.add_message(request, messages.INFO,
                         'You are Successfully Logged Out')
    messages.add_message(request, messages.INFO, 'Thanks for visiting.')
    return HttpResponseRedirect(reverse('Hospital:login'))


# @login_required
def home(request):
    return render(request,"bl/dashboard.html")

@login_required
def experts(request):
    experts = Expert.objects.all()
    
    context = {
        'experts': experts
    }
    return render(request,"bl/experts.html", context)



def addExpert(request):
    if request.method == 'POST':
        new_expert = Expert(
            full_name = request.POST['first_name'] + " " + request.POST['last_name'],
            email = request.POST['email'],
            phone =request.POST['phone'],
            expert_type =  request.POST['expert_type'],
            description = request.POST['description'])

        new_expert.save()
            
        # if request.FILES['icon']:
        #     new_expert.avatar = request.FILES['icon']
        #     new_expert.save()

        messages.success(request, ' Your changes were successfully saved')

        return HttpResponseRedirect(reverse('bl:experts'))

def editExpert(request):
    if request.method == 'POST':
        expert = Expert.objects.get(pk= request.POST['expertid'])
        expert.full_name = request.POST['full_name']
        expert.email = request.POST['email']
        expert.phone =request.POST['phone']
        expert.expert_type =  request.POST['expert_type']
        expert.description = request.POST['description']
        expert.best_dish = request.POST['best_dish']
        expert.rate = request.POST['rate']
        expert.station = request.POST['station']
        expert.availability = request.POST['availability']
        expert.fb = request.POST['fb']
        expert.twitter = request.POST['twitter']
        expert.youtube = request.POST['youtube']
        expert.instagram = request.POST['instagram']
       
        expert.save()
            
        # if request.FILES['icon']:
        #     new_expert.avatar = request.FILES['icon']
        #     new_expert.save()


        messages.info(request, ' Your changes were successfully saved')

        return HttpResponseRedirect(reverse('bl:expertDetail', kwargs={'id': request.POST.get('expertid')}))


@login_required
def expertDetail(request,id):
    expert = Expert.objects.get(pk=id)
    context = {
        'expert': expert
    }

    return render(request,"bl/expert_details.html", context)

def deleteExpert(request, id):
    expert = get_object_or_404(Expert, pk=id).delete()
    messages.error(request, 'You just trashed an expert')
    return HttpResponseRedirect(reverse('bl:experts'))


   

