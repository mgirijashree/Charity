from django.shortcuts import render

from .forms import DonationForm

import json

from django.http import JsonResponse

from django.core.mail import send_mail

from django.conf import settings

from .forms import VolunteerForm

def register_view(request):
    if request.method == 'POST':
        # 1. Bind the POST data to the form
        form = VolunteerForm(request.POST)
        
        # 2. Validate the form
        if form.is_valid():
            # 3. Access the data using form.cleaned_data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            interest = form.cleaned_data['area_of_interest']
            availability = form.cleaned_data['availability']
            
            # Here, you would typically save this to your database
            # Example: Volunteer.objects.create(name=name, ...)
            
            return redirect('success_page') 
    else:
        # Create a blank form for GET requests
        form = Form()
        
    return render(request, 'register.html', {'form': form})



def home(request): return render(request, 'home.html')
def about(request): return render(request, 'about.html')
def causes(request): return render(request, 'causes.html')
def donate(request): return render(request, 'donate.html')
def donate_success(request): return render(request, 'donate_success.html')
def contact(request): return render(request, 'contact.html')
def volunteer(request): return render(request, 'volunteer.html')


from django.shortcuts import render, redirect
from .forms import DonationForm

def donate(request):

    if request.method == "POST":

        form = DonationForm(request.POST)

        if form.is_valid():

            return render(
                request,
                "donate_success.html",
                {
                    "name": form.cleaned_data["name"]
                }
            )

    else:
        form = DonationForm()

    return render(request, "donate.html", {"form": form})

def donate_success(request):

    return render(request, "donate_success.html")





def subscribe_email(request):

    if request.method=="POST":

        data=json.loads(request.body)

        email=data.get("email")

        try:

            send_mail(

                subject="Welcome to HopeHands Foundation",

                message=f"""
Dear Supporter,

Thank you for subscribing to HopeHands Foundation.

You will now receive updates about:

• Charity Programs
• Volunteer Opportunities
• Fundraising Events
• Success Stories

Thank you for supporting our mission.

Regards,
HopeHands Foundation
                """,

                from_email=settings.EMAIL_HOST_USER,

                recipient_list=[email],

                fail_silently=False

            )

            return JsonResponse({

                "status":"success",

                "message":"Confirmation email has been sent."

            })

        except Exception as e:
            print(e)

            return JsonResponse({
                "status":"error",
                "message": str(e)
            })

 