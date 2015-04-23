#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.shortcuts import render
import random
import re


def index_sv(request):
    first_word = [
        'bajsiga',
        'dallrande',
        'degiga',
        'dreglande',
        'dumma',
        'eländiga',
        'enögda',
        'feta',
        'fittiga',
        'fläskiga',
        'fula',
        'gamla',
        'griniga',
        'grisiga',
        'håriga',
        'hästluktande',
        'idiotiska',
        'illaluktande',
        'jiddrande',
        'jobbiga',
        'jäkla',
        'jävla',
        'kebabluktande',
        'kommunistiska',
        'krulliga',
        'kukiga',
        'kuksugande',
        'krökta',
        'köttiga',
        'lata',
        'lallande',
        'leriga',
        'lilla',
        'läskiga',
        'mögliga',
        'ruttna',
        'röviga',
        'rövluktande',
        'patetiska',
        'runkande',
        'skabbiga',
        'sladdriga',
        'slemmiga',
        'snoriga',
        'snuskiga',
        'stora',
        'svettiga',
        'svullna',
        'tjocka',
        'tråkiga',
        'treögda',
        'usla',
        'vårtiga',
        'äckliga',
    ]

    second_word = [
        'bajs',
        'deg',
        'diarre',
        'dum',
        'dummer',
        'dyng',
        'fitt',
        'fläsk',
        'ful',
        'fån',
        'får',
        'gröt',
        'hor',
        'häng',
        'idiot',
        'kiss',
        'kloak',
        'knöl',
        'kuk',
        'lort',
        'lump',
        'lus',
        'mongo',
        'mögel',
        'platt',
        'prakt',
        'prutt',
        'pott',
        'runk',
        'röt',
        'röv',
        'skabb',
        'skit',
        'slabb',
        'sladder',
        'snor',
        'snusk',
        'sopp',
        'sperma',
        'spott',
        'strul',
        'sump',
        'svett',
        'tjock',
        'tång',
        'äckel',
    ]

    third_word = [
        ('Din', 'amöba'),
        ('Din', 'apa'),
        ('Ditt', 'arsle'),
        ('Din', 'babian'),
        ('Din', 'balle'),
        ('Ditt', 'bajveck'),
        ('Din', 'bandit'),
        ('Din', 'blöja'),
        ('Din', 'bulle'),
        ('Ditt', 'cp'),
        ('Ditt', 'dregel'),
        ('Din', 'dåre'),
        ('Ditt', 'drägg'),
        ('Din', 'fejja'),
        ('Ditt', 'fejs'),
        ('Din', 'fitta'),
        ('Din', 'gris'),
        ('Din', 'gråsugga'),
        ('Din', 'gurka'),
        ('Din', 'hora'),
        ('Din', 'häst'),
        ('Din', 'hög'),
        ('Din', 'idiot'),
        ('Ditt', 'juck'),
        ('Din', 'kamel'),
        ('Din', 'klåpare'),
        ('Din', 'korv'),
        ('Din', 'kossa'),
        ('Ditt', 'krull'),
        ('Ditt', 'kräk'),
        ('Din', 'kuk'),
        ('Ditt', 'kött'),
        ('Din', 'limpa'),
        ('Ditt', 'luder'),
        ('Ditt', 'miffo'),
        ('Ditt', 'mongo'),
        ('Ditt', 'monster'),
        ('Din', 'månglare'),
        ('Ditt', 'nylle'),
        ('Din', 'pudding'),
        ('Din', 'skalle'),
        ('Ditt', 'slem'),
        ('Din', 'spya'),
        ('Din', 'svamp'),
        ('Din', 'penis'),
        ('Din', 'potatis'),
        ('Din', 'pung'),
        ('Din', 'påse'),
        ('Din', 'rumpa'),
        ('Din', 'runkare'),
        ('Din', 'räka'),
        ('Din', 'råtta'),
        ('Din', 'röv'),
        ('Din', 'sork'),
        ('Din', 'tratt'),
        ('Ditt', 'troll'),
        ('Din', 'usling'),
        ('Ditt', 'äckel'),
        ('Ditt', 'ägg'),
    ]

    last_word = random.choice(third_word)
    insult = '%s %s %s%s.' % (last_word[0], random.choice(first_word), random.choice(second_word), last_word[1])

    regexp = r"(\w)\1{2,}"
    spell_checked_insult = re.sub(regexp, repl, insult)

    insults = len(first_word) * len(second_word) * len(third_word)

    context = {
        'insult': spell_checked_insult,
        'insults': insults
    }

    return render(request, 'index_sv.html', context)


def repl(m):
    # Switch 'bbb' for 'bb'
    return m.group()[:2]


def index(request):
    context = {
        'insult': 'Fuck off'
    }
    return render(request, 'index.html', context)


def about(request):
    return render_to_response('about.html')


def contact(request):
    return render_to_response('contact.html')
