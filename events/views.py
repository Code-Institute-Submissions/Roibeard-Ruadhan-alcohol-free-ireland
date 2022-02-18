from .models import events
from django.views import generic, View
from blog.models import User
from datetime import datetime
from django.http import HttpResponseRedirect,HttpResponse
from .forms import EventForm
from django.shortcuts import render, redirect
# Create your views here.

class EventList(generic.ListView):
    model = events
    queryset = events.objects.filter(approve = True).order_by("-event_date")
    template_name = "events.html"
    paginate_by = 6
    # upcoming = Event.objects.filter(date__gte=now).order_by('date')
    # passed = Event.objects.filter(date__lt=now).order_by('-date')
    # return list(upcoming) + list(passed)



# @login_required
def add_event(request):
    submitted = False
    form = EventForm()
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            print('mess')
            form.save()
            return redirect('home')
        else:
            form = EventForm
            if 'submitted' in request.POST:
                submitted = True

    return render(request, 'add_event.html', {'form':form, 'submitted':submitted})