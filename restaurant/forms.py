from django import forms
from django_countries.fields import CountryField

from django_countries.widgets import CountrySelectWidget
PAYMENT_CHOICES =(
     ('C','Stripe'),
     ('P','Paypal'),
     ('M','Mpesa'),
     
)
     

 
class CheckoutForm(forms.Form):
     building_name = forms.CharField(widget=forms.TextInput(attrs={
          'class':'form-control'
     }))
     floor_number = forms.CharField(widget=forms.TextInput(attrs={
          'class':'form-control'
     }))
     room_number = forms.CharField(widget=forms.TextInput(attrs={
          'class':'form-control'
     }))
     country = CountryField(blank_label='(select country)').formfield(widget=CountrySelectWidget (attrs={
          'class':'wide w-100'
     }))
     county = forms.CharField(widget=forms.TextInput(attrs={
          'class':'wide w-100'
     }))
     same_billing_address = forms.BooleanField(widget=forms.CheckboxInput())
     save_info = forms.BooleanField(required=False,widget=forms.CheckboxInput())
     payment_option = forms.ChoiceField(required= False,widget=forms.RadioSelect,choices=PAYMENT_CHOICES)

class CouponForm(forms.Form):
     code= forms.CharField(widget=forms.TextInput(attrs={
          'class':'form-control',
          'placeholder':'Promo-code',
          'aria-label':'recepient\'s username',
          'aria-describedby':'basic-addon2'}))

class RefundForm(forms.Form):
     ref_code = forms.CharField()
     message = forms.CharField( widget=forms.Textarea(attrs={
          'row':4
     }))
     email = forms.EmailField()
