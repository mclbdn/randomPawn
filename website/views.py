from django.shortcuts import render
import requests
import json
from random import randint
import re

# Create your views here.


def website(request):
    r = requests.get('https://haveibeenpwned.com/api/v3/breaches')

    data = r.json()

    lst_length = len(data)

    random_breach = randint(0, lst_length)

    title = (data[random_breach]['Title'])
    breachDate = (data[random_breach]['BreachDate'])
    domain = (data[random_breach]['Domain'])
    domain = 'https://www.' + domain
    domain_to_show = (data[random_breach]['Domain'])
    description = (data[random_breach]['Description'])
    description = re.sub('<a.*?>|</a>|<em>|</em>|&quot;', '', description)
    data_compromised = data[random_breach]['DataClasses']

    context = {
        'title': title,
        'breachDate': breachDate,
        'domain': domain,
        'description': description,
        'data_compromised': data_compromised,
        'domain_to_show': domain_to_show
    }

    return render(request, 'base.html', context)
