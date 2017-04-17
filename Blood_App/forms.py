from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.forms import RadioSelect


from models import RegisteredUser,Address,BloodGroup,BloodPouch
import models
class RegistrationForm(forms.Form):
    GENDER_CHOICES = (
        ('Male', 'M'),
        ('Female', 'F')
    )
    BLOOD_TYPES = (
        ('A+', 'A+'),
        ('B+', 'B+'),
        ('AB+', 'O+'),
    )
    email = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    name = forms.CharField(max_length=100)
    city = forms.CharField(max_length=50)
    street = forms.CharField(max_length=50)
    pin = forms.IntegerField()
    blood_group = forms.ChoiceField(choices=BLOOD_TYPES)
    dob = forms.DateField()
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    contact = forms.CharField(max_length=13)

    class Meta:
        model = RegisteredUser
        exclude = ('created_at')



    def is_valid(self):

        valid = super(RegistrationForm,self).is_valid()

        data = self.cleaned_data
        password1 = data['password1']
        password2 = data['password2']

        if password1 != password2:
            valid = False
            self._errors['password1'] = [u'Passwords does not match']
        try:
            User.objects.get(email=data['email'])
            valid = False
            self._errors['email'] = [u'This Email is already in use']
        except User.DoesNotExist:
            pass

        if len(password1) < 6:
            valid = False
            self._errors['password1'] = [u'Password should be atleast 8 characters long']



        return valid

    def save(self,commit=True):

        data = self.cleaned_data
        user = User.objects.create(username=data['email'],email=data['email'],first_name=data['name'])
        user.set_password(data['password1'])
        user.save()

        blood = BloodGroup.objects.create(group=data['blood_group'])

        address = Address.objects.create(street=data['street'],city=data['city'],pin=data['pin'])
        address.save()

        gender = data['gender']
        contact = data['contact']
        dob = data['dob']

        registered = RegisteredUser.objects.create(user=user,address=address,gender=gender,contact=contact,blood_group=blood,dob=dob)

        return registered

class LoginForm(forms.Form):

    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

    def is_valid(self):

        valid = super(LoginForm, self).is_valid()

        data = self.cleaned_data

        username = data['email']
        password = data['password']

        user = authenticate(username=username,password=password)

        if user is not None:
            return user
        else:
            return "No User Found"

class BloodPouch(forms.Form):

    city = forms.CharField(max_length=50)
    street = forms.CharField(max_length=50)
    pin = forms.IntegerField()
    blood_group = forms.ModelChoiceField(queryset=BloodGroup.objects.all())
    donated_by = forms.ModelChoiceField(queryset=RegisteredUser.objects.all())
    quantity = forms.IntegerField()
    cholestrol_level = forms.FloatField()

    def is_valid(self):

        valid = super(BloodPouch, self).is_valid()

        data = self.cleaned_data

        city = data['city']

        street = data['st']

        address = Address.objects.create(city=city)


class DonateForm(forms.ModelForm):
    class Meta:
        model = models.BloodPouch
        fields = ['chlorestrol_level','quantity']





