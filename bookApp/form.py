from django import forms
from .models import Writer,Book

class UserForm(forms.Form):

    user_name=forms.CharField(label='User Name',max_length=20,widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(label='Password',max_length=16,widget=forms.PasswordInput(attrs={'class':'form-control'}))


class WriterForm(forms.ModelForm):

    class Meta:
         
         model = Writer 

         fields = ['firstName','lastName'] 

class BookForm(forms.ModelForm):

    class Meta:

        model = Book   

        fields = ['name','writer']    

        widgets={

            'name': forms.TextInput(attrs={'class': 'form-control mb-3row'}),
            'writer':forms.Select(attrs={'class': 'form-control'}),


        }  