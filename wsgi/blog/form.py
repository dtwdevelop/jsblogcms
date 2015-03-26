from django import forms
from captcha.fields import ReCaptchaField
# from djangular.forms.angular_model import NgModelFormMixin
#NgModelFormMixin,
class Contact(forms.Form):
   
    name = forms.CharField(required=True,max_length=10,widget=forms.TextInput(attrs={'class': 'form-control'}))
    mail  = forms.EmailField(required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
    CHOICES = (('1', 'Ask',), ('2', 'Service',))
    you_type = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    body = forms.CharField(required=True,label='Post your Artitcle',widget=forms.Textarea(attrs={'class': 'form-control'}),max_length=150)
    captcha = ReCaptchaField(
    public_key='6LfnhPwSAAAAAOS7TD1Z1yyYCz3HYctESfwZYCxq',
    private_key='6LfnhPwSAAAAAAsV5yyZgjcDlQi-uBtR8Zb74IwO',
    use_ssl=True
    )
    
class FileUpload(forms.Form):  
    title = forms.CharField()
    file  = forms.FileField()

class Login(forms.Form):
    login = forms.CharField(required=True,max_length=10,widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    
    
class RegisterForm(forms.Form):
        login = forms.CharField(required=True,max_length=10,widget=forms.TextInput(attrs={'class': 'form-control'}))
        mail  = forms.EmailField(required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))

        password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
        password_repeat = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
        CHOICES = (('1', 'agree',), )
        captcha = ReCaptchaField(
    public_key='6LfnhPwSAAAAAOS7TD1Z1yyYCz3HYctESfwZYCxq',
    private_key='6LfnhPwSAAAAAAsV5yyZgjcDlQi-uBtR8Zb74IwO',
    use_ssl=True
    )
       # agree = forms.ChoiceField(required=True,widget=forms.CheckboxInput, choices=CHOICES)
       


    