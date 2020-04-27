from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile, Interests, Role
from django.conf import settings
from PIL import Image
from django.contrib.auth.decorators import login_required
from tinymce import TinyMCE

class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False
class SignupForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget = forms.TextInput(attrs={'placeholder': 'Enter first name'})
        self.fields['last_name'].widget = forms.TextInput(attrs={'placeholder': 'Enter last name'})

    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    description = forms.CharField(widget=TinyMCEWidget(attrs={'required': False, 'cols': 30, 'rows': 10}))
    interests  = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, help_text="Choose your interests", queryset=Interests.objects.all())
    biography = forms.CharField(widget=TinyMCEWidget(attrs={'required': False, 'cols': 30, 'rows': 10}))
    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name',  'name','image', 'fields', 'category', 'description', 'phone', 'facebook', 'twitter', 'skype', 'site', 'address', 'interests' ,'biography')
        help_texts = {
            # 'image': 'Upload profile image',
            'fields': 'Choose your fields',
            'category': 'Choose your category',
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter full name'}),
            # 'description': forms.TextInput(attrs={'placeholder': 'Paste description from your CV'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Enter phone'}),
            'facebook': forms.TextInput(attrs={'placeholder': 'Enter facebook link'}),
            'twitter': forms.TextInput(attrs={'placeholder': 'Enter twitter link'}),
            'skype': forms.TextInput(attrs={'placeholder': 'Enter your skype id'}),
            'site': forms.TextInput(attrs={'placeholder': 'Enter your site'}),
            'address': forms.TextInput(attrs={'placeholder': 'Enter address'}),
            # 'biography': forms.TextInput(attrs={'placeholder': 'Paste biography from your CV'}),
        }


    def signup(self, request, user):
        # Save your user
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

        user.userprofile.name = self.cleaned_data['name']
        user.userprofile.image = self.cleaned_data.get('image')
        user.userprofile.fields = self.cleaned_data['fields']
        user.userprofile.category = self.cleaned_data['category']
        user.userprofile.description = self.cleaned_data['description']
        user.userprofile.phone = self.cleaned_data['phone']
        user.userprofile.facebook = self.cleaned_data['facebook']
        user.userprofile.twitter = self.cleaned_data['twitter']
        user.userprofile.skype = self.cleaned_data['skype']
        user.userprofile.site = self.cleaned_data['site']
        user.userprofile.address = self.cleaned_data['address']
        interests = self.cleaned_data['interests']
        user.userprofile.interests.set(interests)
        user.userprofile.biography = self.cleaned_data['biography']
        role = Role.objects.get(pk=1) #self.cleaned_data['role']#Role.objects.first().pk # Role.objects.all()[0] # role = Role.objects.first()
        user.userprofile.role.add(role)
        user.userprofile.save()


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):

    description = forms.CharField(widget=TinyMCEWidget(attrs={'required': False, 'cols': 30, 'rows': 10})) 
    interests  = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, help_text="Choose your interests", queryset=Interests.objects.all())
    biography = forms.CharField(widget=TinyMCEWidget(attrs={'required': False, 'cols': 30, 'rows': 10}))  

    class Meta:
        model = UserProfile
        fields = ('name', 'image', 'fields', 'category', 'description', 'phone', 'facebook', 'twitter', 'skype', 'site', 'address', 'interests' ,'biography')