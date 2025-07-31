from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Job, Application
from .forms import JobForm, ApplicationForm, UserRegisterForm
from jobs import models
from django.db.models import Q  # Add this line
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.db.models import Q  # Important for search
from .models import Job, Application, User
from .forms import JobForm, ApplicationForm, UserRegisterForm
from django.core.paginator import Paginator



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_applicant = not form.cleaned_data.get('is_employer')
            user.is_employer = form.cleaned_data.get('is_employer')
            user.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'registration/login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('home')

@login_required
def dashboard(request):
    if request.user.is_employer:
        jobs = Job.objects.filter(posted_by=request.user)
        return render(request, 'jobs/employer_dashboard.html', {'jobs': jobs})
    else:
        applications = Application.objects.filter(applicant=request.user)
        return render(request, 'jobs/applicant_dashboard.html', {'applications': applications})


@login_required
def post_job(request):
    if not request.user.is_employer:
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.posted_by = request.user
            job.save()
            return redirect('dashboard')
    else:
        form = JobForm()
    return render(request, 'jobs/post_job.html', {'form': form})

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# @login_required
def job_list(request):
    query = request.GET.get('q')
    page = request.GET.get('page', 1)  # Default to first page
    
    if query:
        jobs = Job.objects.filter(
            Q(title__icontains=query) |
            Q(company_name__icontains=query) |
            Q(location__icontains=query)
        ).distinct().order_by('-created_at')  # Newest first
    else:
        jobs = Job.objects.all().order_by('-created_at')  # Newest first

    # Pagination with 10 jobs per page
    paginator = Paginator(jobs, 6)
    
    try:
        jobs_page = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page
        jobs_page = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver last page
        jobs_page = paginator.page(paginator.num_pages)

    return render(request, 'jobs/job_list.html', {
        'jobs': jobs_page,
        'query': query  # Pass query back to template
    })

@login_required
def job_detail(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    if request.method == 'POST' and not request.user.is_staff:
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.applicant = request.user
            application.save()
            return redirect('dashboard')
    else:
        form = ApplicationForm() if not request.user.is_staff else None
    
    return render(request, 'jobs/job_detail.html', {
        'job': job,
        'form': form,
        'can_apply': not request.user.is_staff and not Application.objects.filter(job=job, applicant=request.user).exists()
    })

@login_required
def view_applicants(request, job_id):
    if not request.user.is_employer:
        return redirect('dashboard')

    job = get_object_or_404(Job, id=job_id, posted_by=request.user)
    applicants = Application.objects.filter(job=job).select_related('applicant')

    # Update status to 'reviewed' if not already
    applicants.exclude(status='reviewed').update(status='reviewed')

    return render(request, 'jobs/view_applicants.html', {
        'job': job,
        'applicants': applicants
    })