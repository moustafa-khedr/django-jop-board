from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Job
from django.core.paginator import Paginator
from .form import ApplyForm, AddForm
from django.urls import reverse

# Create your views here.

def job_list(request):
    job_list = Job.objects.all()

    paginator = Paginator(job_list, 3)    # Show 25 contacts per page.(كام وظيفة تظهر فى الصفحة )
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'jobs': page_obj}  # template name      (page_obj  بضيفها مكان jop list لانها بترجع بكام وظيفة فى الصفحة)
    return render(request, 'job/job_list.html', context)


def job_detail(request, slug):
    job_detail = Job.objects.get(slug=slug)

    if request.method == 'POST':
        form = ApplyForm(request.POST, request.FILES)
        print('post')
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job = job_detail
            myform.save()
            print('save done')

    else:
        form = ApplyForm()

    context = {'job': job_detail, 'form': form}
    return render(request, 'job/job_detail.html', context)

@login_required
def add_job(request):

    if request.method == 'POST':
        form = AddForm(request.POST, request.FILES)   # requset FIles fro image save
        print("POST")
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user         # request.user =  a person who is login now and do this
            myform.save()
            print('POST SAVE')
            return redirect(reverse('jobs:job_list'))
    else:
        form = AddForm

    return render(request, 'job/add_job.html', {'form':form})
