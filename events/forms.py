from django import forms
from django.forms import ModelForm
from .models import events
# from .widgets import DatePickerInput, TimePickerInput, DateTimePickerInput

class EventForm(ModelForm):
    class Meta:
        model = events
        # my_date_field = forms.DateField(widget=DatePickerInput)
        # my_time_field = forms.TimeField(widget=TimePickerInput)
        # my_date_time_field = forms.DateTimeField(widget=DateTimePickerInput)

        fields = ('location', 'venue', 'venue_image', 'event_date', 'description')

       

        labels = {
            'venue_image': 'venue_image',
        }
        widgets = {
            'event_date': forms.DateInput(attrs={'type': 'date', 'placeholder': 'Date'}),
        }
 

        #Removed labels & widgets as fields will suffice
        # labels = {
        #     # 'organiser': 'User'
        #     'location': 'County/Town',
        #     'venue': 'Venue',
        #     'venue_image': 'venue_image',
        #     'event_date': 'Event Date',
        #     'guest_limit': 'Max Attendees',
        #     'description': 'Description',
        # }
        # widgets = {
        #     'location': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Location'}),
        #     'venue': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Venue'}),
        #     'venue_image': forms.ClearableFileInput((attrs={'class':'form-control', 'placeholder':'Venue-Image'}),
        #     'event_date': forms.DateInput(attrs={'class':'form-control', 'type': 'date', 'placeholder':'YYYY-MM-DD HH:MM:SS'}),
        #     'guest_limit': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Maximum number that can attend'}),
        #     'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Arrival time & other details'}),
        # }