import requests

server_data = {
    'cao': {
        'url': 'http://crawl.akrasiac.org',
        'rc': 'rcfiles/crawl-git',
        'morgue': 'rawdata',
    },
    'cdo': {
        'url': 'http://crawl.develz.org',
        'rc': 'configs/trunk',
        'morgue': 'morgues/trunk',
    },
    'cszo': {
        'url': 'http://dobrazupa.org',
        'rc': 'rcfiles/crawl-git',
        'morgue': 'morgue',
    },
}

class Server(object):

    def __init__(self, name, url, rc, morgue):
        self.name = name
        self.url = url
        self._rc = rc
        self._morgue = morgue
    
    @property
    def rc(self):
        return '%s/%s' % (self.url, self._rc)

    @property
    def morgue(self):
        return u'%s/%s' % (self.url, self._morgue)

# 'Server' instances
cao = Server('cao', **server_data['cao'])
cdo = Server('cdo', **server_data['cdo'])
cszo = Server('cszo', **server_data['cszo'])

# this passphrase is used if one isn't present in the settings module
default_passphrase = 'dieselrobin'

servers = {
    'cao': cao,
    'cdo': cdo,
    'cszo': cszo,
}

def check_rc_file(server, player):
    '''
    Check a player's rcfile for a passphrase. Used for initial registration.

    Returns True for a match, otherwise False.
    '''
    fname = player + '.rc'
    passphrase = default_passphrase
    req_url = '/'.join([servers[server].rc, fname]) 
    response = requests.get(req_url)
    if str(response.iter_lines().next().strip()) == passphrase:
        return True
    return False

# combo data
# TODO: generate valid combo list

DG = ('be', 'ak', 'ck', 'dk', 'pr', 'he')
FE = ('gl', 'hu', 'as', 'ar', 'am')
DS = VP = UNDEAD = ('pr', 'he')
GH = MU = UNDEAD + ('tm',)

class ComboData(object):
    def __init__(self):
        self.races = {
            # field 3 of the tuple is class restrictions
            'hu': ('Hu', 'Human', None),
            'he': ('HE', 'High Elf', None),
            'de': ('DE', 'Deep Elf', None),
            'se': ('SE', 'Sludge Elf', None),
            'dd': ('DD', 'Deep Dwarf', None),
            'ho': ('HO', 'Hill Orc', None),
            'mf': ('Mf', 'Merfolk', None),
            'ha': ('Ha', 'Halfling', None),
            'ko': ('Ko', 'Kobold', None),
            'sp': ('Sp', 'Spriggan', None),
            'na': ('Na', 'Naga', None),
            'ce': ('Ce', 'Centaur', None),
            'og': ('Og', 'Ogre', None),
            'tr': ('Tr', 'Troll', None),
            'mi': ('Mi', 'Minotaur', None),
            'te': ('Te', 'Tengu', None),
            'dr': ('Dr', 'Draconian', None),
            'dg': ('Dg', 'Demigod', DG),
            'ds': ('Ds', 'Demonspawn', DS),
            'mu': ('Mu', 'Mummy', MU),
            'gh': ('Gh', 'Ghoul', GH),
            'vp': ('Vp', 'Vampire', VP),
            'fe': ('Fe', 'Felid', FE),
            'op': ('Op', 'Octopode', None),
        }

        self.classes = {
            'fi': ('Fi', 'Fighter'),
            'gl': ('Gl', 'Gladiator'),
            'mo': ('Mo', 'Monk'),
            'hu': ('Hu', 'Hunter'),
            'as': ('As', 'Assassin'),
            'ar': ('Ar', 'Artificer'),
            'be': ('Be', 'Berserker'),
            'ak': ('AK', 'Abyssal Knight'),
            'ck': ('CK', 'Chaos Knight'),
            'dk': ('DK', 'Death Knight'),
            'pr': ('Pr', 'Priest'),
            'he': ('He', 'Healer'),
            'sk': ('Sk', 'Skald'),
            'tm': ('Tm', 'Transmuter'),
            'wr': ('Wr', 'Warper'),
            'am': ('AM', 'Arcane Marksman'),
            'en': ('En', 'Enchanter'),
            'wz': ('Wz', 'Wizard'),
            'cj': ('Cj', 'Conjurer'),
            'su': ('Su', 'Summoner'),
            'ne': ('Ne', 'Necromancer'),
            'fe': ('FE', 'Fire Elementalist'),
            'ie': ('IE', 'Ice Elementalist'),
            'ae': ('AE', 'Air Elementalist'),
            'ee': ('EE', 'Earth Elementalist'),
            'vm': ('VM', 'Venom Mage'),
        }

combo_data = ComboData()

def valid_character(race, cls):
    race, cls = race.lower(), cls.lower()
    short, long, restricted = combo_data.races[race]
    return not cls in restricted if restricted else True

VALID_CHARACTERS = tuple(
    ((race + cls, race_data[0] + cls_data[0]) 
        for race, race_data in combo_data.races.items()
        for cls, cls_data in combo_data.classes.items()
        if valid_character(race, cls)
    )
)

if __name__ == '__main__':
    races, classes = ['mi', 'mu', 'ho', 'fe'], ['dk', 'tm', 'be', 'gl']
    tests = zip(races, classes)
    for test in tests:
        print test, valid_character(*test)
    chars = sorted([can for s, can in VALID_CHARACTERS])
    print len(chars)
    print ', '.join(chars)

