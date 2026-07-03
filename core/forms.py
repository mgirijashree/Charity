from django import forms
from django.core.validators import RegexValidator


CAUSE_CHOICES = [
    ("", "Select a Cause"),
    ("education", "Education for Children"),
    ("healthcare", "Healthcare Support"),
    ("food", "Food & Shelter"),
    ("disaster", "Disaster Relief"),
]

AREA_CHOICES = [

    ("","Select Area of Interest"),

    ("education","Education Support"),

    ("medical","Medical Assistance"),

    ("food","Food Distribution"),

    ("events","Event Coordination"),

    ("online","Online Volunteering"),

]

AVAILABILITY_CHOICES = [

    ("","Select Availability"),

    ("weekdays","Weekdays"),

    ("weekends","Weekends"),

    ("fulltime","Full Time"),

    ("parttime","Part Time"),

    ("remote","Remote"),

]
 

class DonationForm(forms.Form):

    name = forms.CharField(
        label="",
        min_length=3,
        max_length=100,
        validators=[
            RegexValidator(
                regex=r'^[A-Za-z ]+$',
                message="Name should contain only alphabets."
            )
        ],
        widget=forms.TextInput(attrs={
            "placeholder": "Full Name",
            "class": "w-full rounded-lg border border-gray-300 px-4 py-3 focus:ring-2 focus:ring-blue-700 focus:outline-none"
        })
    )

    email = forms.EmailField(
    widget=forms.EmailInput(
        attrs={
            "placeholder": "Email Address",
            "class": "w-full rounded-lg border border-gray-300 px-4 py-3"
        }
    )
)

    
    phone = forms.CharField(
        label="",
        max_length=10,
        min_length=10,
        validators=[
            RegexValidator(
                regex=r'^\d{10}$',
                message="Phone number must contain exactly 10 digits."
            )
        ],
        widget=forms.TextInput(attrs={
            "placeholder": "Phone Number",
            "maxlength": "10",
            "class": "w-full rounded-lg border border-gray-300 px-4 py-3 focus:ring-2 focus:ring-blue-700 focus:outline-none"
        })
    )

    address = forms.CharField(
        label="",
        widget=forms.Textarea(attrs={
            "rows": 3,
            "placeholder": "Address",
            "class": "w-full rounded-lg border border-gray-300 px-4 py-3 resize-none focus:ring-2 focus:ring-blue-700 focus:outline-none"
        })
    )

    amount = forms.IntegerField(
        widget=forms.HiddenInput()
    )

    cause = forms.ChoiceField(
        choices=CAUSE_CHOICES,
        widget=forms.Select(attrs={
            "class": "w-full rounded-lg border border-gray-300 px-4 py-3"
        })
    )

    payment_method = forms.CharField(
        required=False,
        widget=forms.HiddenInput()
    )

    def clean_amount(self):

        amount = self.cleaned_data["amount"]

        if amount < 100:
            raise forms.ValidationError(
                "Minimum donation amount is ₹100."
            )

        return amount


class VolunteerForm(forms.Form):

    name=forms.CharField(

        min_length=3,

        max_length=100,

        validators=[

            RegexValidator(

                regex=r'^[A-Za-z ]+$',

                message="Name should contain only alphabets."

            )

        ],

        widget=forms.TextInput(attrs={

            "class":"w-full border rounded-lg px-4 py-3",

            "placeholder":"Enter your full name"

        })

    )

    email=forms.EmailField(

        widget=forms.EmailInput(attrs={

            "class":"w-full border rounded-lg px-4 py-3",

            "placeholder":"Enter your email"

        })

    )

    phone=forms.CharField(

        validators=[

            RegexValidator(

                regex=r'^\d{10}$',

                message="Phone number must contain exactly 10 digits."

            )

        ],

        widget=forms.TextInput(attrs={

            "class":"w-full border rounded-lg px-4 py-3",

            "maxlength":"10",

            "placeholder":"Enter your mobile number"

        })

    )

    area=forms.ChoiceField(

        choices=AREA_CHOICES,

        widget=forms.Select(attrs={

            "class":"w-full border rounded-lg px-4 py-3"

        })

    )

    availability=forms.ChoiceField(

        choices=AVAILABILITY_CHOICES,

        widget=forms.Select(attrs={

            "class":"w-full border rounded-lg px-4 py-3"

        })

    )

    message=forms.CharField(

        required=False,

        widget=forms.Textarea(attrs={

            "rows":4,

            "class":"w-full border rounded-lg px-4 py-3",

            "placeholder":"Tell us why you would like to volunteer..."

        })

    )
class VolunteerForm(forms.Form):
    # Field definitions with labels and placeholders
    name = forms.CharField(
        label="Full Name",
        min_length=3,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your full name', 'class': 'w-full p-3 border rounded bg-gray-50'})
    )
    
    email = forms.EmailField(
        label="Email ID",
        widget=forms.EmailInput(attrs={'placeholder': 'example@mail.com', 'class': 'w-full p-3 border rounded bg-gray-50'})
    )
    
    phone = forms.CharField(
        label="Phone Number",
        validators=[RegexValidator(r'^\d{10}$', 'Phone number must be 10 digits')],
        widget=forms.TextInput(attrs={'placeholder': '9876543210', 'class': 'w-full p-3 border rounded bg-gray-50'})
    )
    
    # Auto-populated Dropdowns
    area_of_interest = forms.ChoiceField(
        label="Area of Interest",
        choices=[('', 'Select your area'), ('education', 'Education'), ('healthcare', 'Healthcare'), ('poverty', 'Poverty Relief')],
        widget=forms.Select(attrs={'class': 'w-full p-3 border rounded bg-gray-50'})
    )
    
    availability = forms.ChoiceField(
        label="Availability",
        choices=[('', 'Select your availability'), ('weekdays', 'Weekdays'), ('weekends', 'Weekends'), ('flexible', 'Flexible')],
        widget=forms.Select(attrs={'class': 'w-full p-3 border rounded bg-gray-50'})
    )