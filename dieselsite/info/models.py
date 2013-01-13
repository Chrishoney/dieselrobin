from django.db import models

DOC_TYPES = (
    ('rules', 'Rules'),
    ('bonus', 'Bonus Missions'),
)

class Document(models.Model):
    '''
    Store a markdown document that will be converted to html in the template.
    
    The documents are stored in the docs folder inside the project root. The
    manage.py command that populates the initial database will insert one row
    for each document type.
    '''
    type = models.CharField(max_length=7, unique=True, choices=DOC_TYPES)
    data = models.TextField()

    def __unicode__(self):
        return u'doc type: %s' % self.type
