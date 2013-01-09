from django.db import models

# The reason for the related_name field string interpolation is explained here:
# https://docs.djangoproject.com/en/1.4/topics/db/models/#be-careful-with-related-name

# choice tuples
REGULAR_CHOICES = tuple((n, str(n)) for n in xrange(1, 15))
BONUS_CHOICES = tuple(REGULAR_CHOICES[:3])

class MissionBase(models.Model):
    '''
    Abstract base class that contains data in common to both mission types
    
    This model cannot be instantiated directly, you must subclass it.
    '''
    player = models.ForeignKey(
        'diesel.Player', blank=True, null=True, related_name='%(class)s_missions'
    )
    combo = models.ForeignKey(
        'diesel.Character', blank=True, null=True, related_name='%(class)s_missions'
    )
    description = models.TextField()
    complete = models.BooleanField(default=False)

    class Meta:
        abstract = True

class Regular(MissionBase):
    number = models.PositiveSmallIntegerField(choices=REGULAR_CHOICES)
    failed = models.BooleanField(default=False)
    new_locations = models.CharField(
        max_length=255, help_text="New locations allowed by this mission"
    )

    class Meta:
        verbose_name_plural = 'Regular'

    def __unicode__(self):
        return u'Regular Mission %s' % self.number

class Bonus(MissionBase):
    tier = models.PositiveSmallIntegerField(choices=BONUS_CHOICES)
    number = models.PositiveSmallIntegerField(choices=BONUS_CHOICES)

    class Meta:
        verbose_name_plural = 'Bonus'

    def __unicode__(self):
        return u'Bonus Mission: Tier %s, Mission %s' % (self.tier, self.number)
