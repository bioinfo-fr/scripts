# -*- coding: utf-8 -*-
import random
import os
import sys

# a fake data generator
from faker import Factory
fake = Factory.create(locale='fr_FR')

syst_encoding = sys.getdefaultencoding()

# some constants
GENDERS = [u'Male', u'm', u'M', u'men', u'Man', u'Men', u'Man', u'Female', u'f', u'w', u'Woman', u'women', u'Women', u'female', u'F']

DEPTS = [
    u'Charente', u'Puy-de-DEme', u'Puy de D^ome', u'Puy de Dôme' 'Puy-De-Dome', u'Lot-et-Garonne',
    u'Lot et Garonne', u'Lot-Et-Garonne', u'Vosges', u'Voges', u'vosges', u'Vosge', u'Tarn', u'Orne', u'Eure',
    u'Ardèche', u'Seine-et-Loire', u'Guadeloupe', u'Corrèze', u'Alpes-Maritimes', u'Alpes-Martitimes',
    u'Seine-Saint-Denis', u'93', u'Gironde', u'Gyronde', u'gironde', u'Manche', u'Maine-et-Loire', u'Maine et Loire',
    u'Guyane', u'Corse', u'Moselle', u'Alpes-de-Haute-Provence', u'Alpes-Haute-Provence', u'Alpes Haute Provence',
    u'Pas-de-Calais', u'Martinique'
]

NATIONALITIES = [u'fr', u'Français', u'FR', u'french', u'DE', u'German', u'ENglish', u'english', u'EN']

HEADERS = [
    u'Patient id', u'Name', u'Lastname', u'gender', u'Nationality', u'Adress', u'Department', u'phone number', u'email'
]


def get_line():
    line = [
        str(random.randint(1, 99999)),
        fake.first_name(),
        fake.last_name(),
        random.choice(GENDERS),
        random.choice(NATIONALITIES),
        fake.address().replace(os.linesep, ' '),
        random.choice(DEPTS),
        random.choice([1, 1, 1, 0]) and fake.phone_number() or u'',
        random.choice([1, 0, 0, 0]) and fake.safe_email() or random.choice([u'', u'.', u' ', u'-'])
    ]
    return line

if __name__ == '__main__':
    separator = '\t'
    print separator.join(HEADERS)
    for x in xrange(500):
        line = separator.join(get_line())
        try:
            print line
        except UnicodeEncodeError:
            print line.encode('utf-8')
