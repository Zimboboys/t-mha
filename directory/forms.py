from django import forms
from directory.models import Cat
from directory.models import Document 

class IntakeForm(forms.ModelForm):
    class Meta:
        model = Cat
        fields = [
            'name', 'gender', 'age', 'description', 'breed', 'itype', 'status',
            'arrival_date', 'arrival_details', 'medical_history', 'vaccinations',
            'is_microchipped', 'flea_control_date', 'deworming_date', 'fiv_felv_date', 
            'special_needs', 'personality', 'more_personality', 'comments', 
            'personal_exp'
        ]

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['document', 'description']