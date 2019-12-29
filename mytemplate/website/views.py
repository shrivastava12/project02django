from django.views.generic import TemplateView

class Homepageview(TemplateView):
    template_name = 'home.html'

class AboutpageView(TemplateView):
    template_name = 'about.html'


class Contact(TemplateView):
    template_name = 'Contactus.html'