# -*- coding: utf-8 -*-
# import traceback

from django.core import serializers
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt

from .models import SalePoint, Contact, InsuranceRequest, SiteFields
from .forms import InsuranceRequestForm


def salepoint(request):
    data = serializers.serialize('json', SalePoint.objects.all())
    return HttpResponse(data, content_type='json')


@csrf_exempt
def contact(request):
    contact_name = request.POST.get('name', '')
    contact_email = request.POST.get('email', '')
    form_content = request.POST.get('message', '')

    if contact_name and len(contact_email > 5):
        new_contact = Contact(
            name=contact_name,
            email=contact_email,
            text=form_content
            )
        new_contact.save()

        template = get_template('contact.txt')
        context = Context({
            'contact_name': new_contact.name,
            'contact_email': new_contact.email,
            'form_content': new_contact.text,
        })
        content = template.render(context)

        email = EmailMessage(
            "New contact form submission",
            content,
            "Your website" + '<hi@superbag.com.ua>',
            ['lucy@superbag.com.ua'],
            headers={'Reply-To': contact_email}
        )
        email.send()
        return HttpResponse('ok')


class HomePageView(TemplateView):

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['latest_articles'] = SalePoint.objects.all()
        fields_dict = {}
        for field in SiteFields.objects.filter(language='ua'):
            fields_dict[field.title] = field.text
        context['fields'] = fields_dict
        return context


class HomePageViewRu(TemplateView):

    template_name = "ru/index.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageViewRu, self).get_context_data(**kwargs)
        context['latest_articles'] = SalePoint.objects.all()
        fields_dict = {}
        for field in SiteFields.objects.filter(language='ru'):
            fields_dict[field.title] = field.text
        context['fields'] = fields_dict
        return context


class LostBaggage(CreateView):
    model = InsuranceRequest
    template_name = 'lost_baggage.html'
    form_class = InsuranceRequestForm

    def get_context_data(self, **kwargs):
        context = super(LostBaggage, self).get_context_data(**kwargs)
        context['text'] = SiteFields.objects.get(
            title="Lost baggage",
            language='ua').text
        return context


class LostBaggageRu(CreateView):
    model = InsuranceRequest
    template_name = 'ru/lost_baggage.html'
    form_class = InsuranceRequestForm

    def get_context_data(self, **kwargs):
        context = super(LostBaggageRu, self).get_context_data(**kwargs)
        context['text'] = SiteFields.objects.get(
            title="Lost baggage",
            language='ru').text
        return context


class CreateRequest(CreateView):
    model = InsuranceRequest
    template_name = 'lost_baggage.html'
    form_class = InsuranceRequestForm

    def post(self, request):
        form = InsuranceRequestForm(request.POST)
        if form.is_valid():
            form.save()
            form.send_form()

            return HttpResponse('Form saved')
        else:
            return HttpResponse('Form doesnt valid')
