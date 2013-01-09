import requests
from django.conf import settings

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
    response = requests.get('/'.join([rcfiles[server], player])
    if response.iter_lines().next().strip() == passphrase:
        return True
    return False
