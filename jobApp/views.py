from django.shortcuts import render
from .models import Job

# Create your views here.
def index(request):
    jobs = Job.objects.all()
    context = {
        "jobs": jobs
    }
    return render(request, "jobApp/index.html", context)
