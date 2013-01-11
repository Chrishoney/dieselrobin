from collections import namedtuple

import requests

from django.conf import settings

SERVER_NAMES = ('cao', 'cdo', 'cszo')

rcfiles = {
    'cao': 'http://crawl.akrasiac.org/rcfiles/crawl-git',
    'cdo': 'http://crawl.develz.org/configs/trunk',
    'cszo': 'http://dobrazupa.org/rcfiles/crawl-git',
}

# this passphrase is used if one isn't present in the settings module
default_passphrase = 'dieselrobin'

def check_rc_file(server, player):
    '''
    Check a player's rcfile for a passphrase. Used for initial registration.

    Returns True for a match, otherwise False.
    '''
    passphrase = getattr(settings, 'PASSPHRASE', default_passphrase)
    response = requests.get('/'.join([rcfiles[server], player]))
    if response.iter_lines().next().strip() == passphrase:
        return True
    return False

# valid combos algo

#TODO: add all the data to this dictionary
combo_data = {
    'race': {
        'hu': ('Hu', 'Human'), 'he': ('HE', 'High Elf')
    },
    'class': {
        'as': ('As', 'Assassin'), 'ar': ('Ar', 'Artificer')
    },
}

# TODO: change this to use the abbreviations dict
#
# disallowed

DG = ('be', 'ak', 'ck', 'dk', 'pr', 'he')
FE = ('gl', 'hu', 'as', 'ar', 'am')
DS = VP = UNDEAD = ('pr', 'he')
GH = MU = UNDEAD + ('tm',)

restricted_races = {
    'dg': DG,
    'fe': FE,
    'ds': DS,
    'vp': VP,
    'gh': GH,
    'mu': MU
}
