from django import forms
from .models import Writer,Book,FavBookCollection
from django.forms.widgets import DateInput

class UserForm(forms.Form):

    user_name=forms.CharField(label='User Name',max_length=20,widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(label='Password',max_length=16,widget=forms.PasswordInput(attrs={'class':'form-control'}))


class WriterForm(forms.ModelForm):

    class Meta:
         
         model = Writer 

         fields = ['firstName','lastName','dob'] 

         widgets ={
             'dob': DateInput(attrs={'type': 'date'})
         }

class BookForm(forms.ModelForm):

    class Meta:

        model = Book   

        fields = ['name','writer','book_Img']   

        widgets={

            'name': forms.TextInput(attrs={'class': 'form-control mb-3row'}),
            'writer':forms.Select(attrs={'class': 'form-control', 'option':'sletcted'}),
            # 'image':forms.ImageField(attrs={'name':'image'}),
            

        }  

class FavBookForm(forms.ModelForm):

    class Meta:

        model = FavBookCollection
        fields='__all__'
       
        widgets={
        'collect_name':forms.TextInput(attrs={'class':'form-control col-6'}),
        'books':forms.SelectMultiple(attrs={'class':'form-select col-6'}),
         }
