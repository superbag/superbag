# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.core.mail import send_mail, EmailMessage
from django.forms import ModelForm
from django.template import Context
from django.template.loader import get_template

from .models import InsuranceRequest


class InsuranceRequestForm(ModelForm):
    class Meta:
        model = InsuranceRequest
        fields = [
            'author', 'phone', 'email', 'airport_arrival', 'ticket_num',
            'airport_destination', 'event_date', 'description', 'info'
        ]

    def save(self):
        data = self.cleaned_data
        req = InsuranceRequest(
                author=data['author'],
                phone=data['phone'],
                email=data['email'],
                airport_arrival=data['airport_arrival'],
                airport_destination=data['airport_destination'],
                ticket_num=data['ticket_num'],
                event_date=data['event_date'],
                description=data['description'],
                info=data['info']
                )
        req.save()
        return

    def send_form(self):
        data = self.cleaned_data
        template = get_template('insurance_request.txt')

        context = Context({
            'author': data['author'],
            'phone': data['phone'],
            'email': data['email'],
            'airport_arrival': data['airport_arrival'],
            'airport_destination': data['airport_destination'],
            'ticket_num': data['ticket_num'],
            'event_date': data['event_date'],
            'description': data['description'],
            'info': data['info']
        })
        content = template.render(context)
        # send_mail(
        #     "Талон {} от {}".format(data['ticket_num'], data['author']),
        #     content,
        #     "Your website" + '<hi@superbag.com.ua>',
        #     # ['superbag@zlagoda.ua', 'hi@superbag.com.ua'],
        # )
        email = EmailMessage(
            u"Талон {} от {}".format(data['ticket_num'], data['author']),
            content,
            "Superbag" + '<hi@superbag.com.ua>',
            ['superbag@zlagoda.ua', 'hi@superbag.com.ua'],
        )
        email.send()
        return
