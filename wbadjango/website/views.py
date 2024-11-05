from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def home(request):
    return render(request, 'home.html', {})

def klachten(request):
    return render(request, 'klachten.html', {})

def adresenroute(request):
    return render(request, 'adresenroute.html', {})

def onsteam(request):
    return render(request, 'onsteam.html', {})

def openingstijden(request):
    return render(request, 'openingstijden.html', {})


def dienstapo(request):
    return render(request, 'dienstapo.html', {})

def privacy(request):
    return render(request, 'privacy.html', {})

def afhaalkluis(request):
    return render(request, 'afhaalkluis.html', {})


def inloop(request):
    return render(request, 'inloop.html', {})

def voorl(request):
    return render(request, 'voorl.html', {})

def iemandanders(request):
    return render(request, 'iemandanders.html', {})

def toest(request):
    return render(request, 'toest.html', {})
def contact(request):
    if request.method == 'POST':
        c_fname = request.POST.get('c_fname')
        c_lname = request.POST.get('c_lname')
        c_email = request.POST.get('c_email')
        c_subject = request.POST.get('c_subject')
        c_message = request.POST.get('c_message')

        message = Mail(
            from_email='apotheekwesterbork@gmail.com',
            to_emails='s.chentasingh@apotheekwesterbork.nl',  # Change to your email
            subject=c_subject,
            html_content=f"<strong>From:</strong> {c_fname} {c_lname}<br>"
                          f"<strong>Email:</strong> {c_email}<br>"
                          f"<strong>Message:</strong><br>{c_message}"
        )

        try:
            sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
            response = sg.send(message)
            return render(request, 'contact.html', {'c_fname'})
        except Exception as e:
            return HttpResponse(f'An error occurred: {e}')

    return render(request, 'contact.html')  # Adjust to your template name
