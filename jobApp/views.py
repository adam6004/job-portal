from django.shortcuts import render
from .models import Job
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    jobs = Job.objects.all()
    context = {
        "jobs": jobs
    }
    return render(request, "jobApp/index.html", context)

def details(request, id):
    job = get_object_or_404(Job, pk=id)
    context = {
        "job": job
    }
    return render(request, "jobApp/details.html", context)
