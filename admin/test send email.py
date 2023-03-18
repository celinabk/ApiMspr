import json

from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect

def send_email(request):
    subject = request.POST.get('subject', 'Test')
    message = request.POST.get('message', 'Hello my name is birane')
    from_email = request.POST.get('from_email', 'iranesamb9@gmail.com')
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, ['iranesamb9@gmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('/contact/thanks/')
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Make sure all fields are entered and valid.')


import requests
"""myjson ={
        "username":"root",
        "password":"root"}
    # request to get token
url ='http://127.0.0.1:8000/api/token/'
data = requests.post(url, json=myjson).text
tokens = json.loads(data)

print(tokens)"""
from django.core.mail import EmailMessage
from django.conf import settings

message = "Test"
subject = 'Qrcode'
send_mail(subject, message, settings.EMAIL_HOST_USER, ['biranebs96@gmail.com'])
email_message = EmailMessage()
EMAIL_HOST_USER = 'biranesamb9@gmail.com'
email_message= EmailMessage(subject, message, settings.EMAIL_HOST_USER)
email_message.attach_file('qrcode.png')
email_message.send()

