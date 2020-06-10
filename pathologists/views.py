# Python packages
import re

# Django imports
from django.shortcuts import redirect, render

# Import my own content
from pathologists.models import Message, Pathologist
from pathologists.forms import PathologistForm


def home(request):

    print(request.method)
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        message = request.POST.get('new-message-input')

        user = None
        if message.startswith('#'):
            # Get the user name from the beginning of the message
            user_name = message.split(' ')[0]
            message = message.replace(user_name, '').strip()

            # Remove any non letter characters
            user_name = re.sub('[^a-zA-Z]', '', user_name)
            user = Pathologist.objects.filter(name__iexact=user_name).first()
            if user_name and not user:
                user = Pathologist.objects.create(name=user_name)

        Message.objects.create(user=user, text=message)

        print(message)
    messages = Message.objects.all().order_by('time')
    return render(request, 'home.html', {'messages': messages})


def profiles(request):
    print('profiles')
    if request.method == 'GET':
        pathologists = Pathologist.objects.all()
        form = PathologistForm()
        return render(request, 'profiles.html', {'pathologists': pathologists, 'form': form})
    elif request.method == 'POST':
        form = PathologistForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            location = form.cleaned_data['location']
            specialty = form.cleaned_data['specialty']

            pathologist = Pathologist.objects.filter(name=name).first()
            if not pathologist:
                Pathologist.objects.create(name=name, location=location, specialty=specialty)
        return redirect('/pathologists/profiles/')