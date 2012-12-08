from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()

    class Meta:
        ordering = ('start_date',)

    def __unicode__(self):
        return '%s' % self.name


class Team(models.Model):
    name = models.CharField(max_length=100)
    event = models.ForeignKey('event.Event', related_name='teams')

    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return self.name


class Player(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(null=True, default=None, blank=True)
    gender = models.IntegerField(choices=((1, 'male'), (2, 'female')))
    birthdate = models.DateField()

    class Meta:
        verbose_name = 'Participant'
        verbose_name_plural = 'Participants'
        ordering = ('lastname',)

    def __unicode__(self):
        return self.full_name

    @property
    def full_name(self):
        return u'%s %s' % (self.firstname, self.lastname,)


class Participation(models.Model):
    player = models.ForeignKey('event.Player', related_name='participations')
    team = models.ForeignKey('event.Team', related_name='participations')
    startnumber = models.IntegerField(blank=True, null=True, default=None)
    giant_slalom_equipment = models.ForeignKey('equipment.GiantSlalomEquipment')
    giant_slalom_time_minutes = models.IntegerField(null=True, default=None, blank=True)
    giant_slalom_time_seconds = models.IntegerField(null=True, default=None, blank=True)
    giant_slalom_time_hundredths = models.IntegerField(null=True, default=None, blank=True)
    giant_slalom_did_not_start = models.BooleanField()
    giant_slalom_did_not_finish = models.BooleanField()
    giant_slalom_disqualified = models.BooleanField()
    jump_equipment = models.ForeignKey('equipment.JumpEquipment')
    jump_one_distance = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=None, blank=True)
    jump_two_distance = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=None, blank=True)
    jump_did_not_start = models.BooleanField()
    jump_did_not_finish = models.BooleanField()
    jump_disqualified = models.BooleanField()
    cross_country_time_minutes = models.IntegerField(null=True, default=None, blank=True)
    cross_country_time_seconds = models.IntegerField(null=True, default=None, blank=True)
    cross_country_time_hundredths = models.IntegerField(null=True, default=None, blank=True)
    cross_country_did_not_start = models.BooleanField()
    cross_country_did_not_finish = models.BooleanField()
    cross_country_disqualified = models.BooleanField()
    swimming_time_minutes = models.IntegerField(null=True, default=None, blank=True)
    swimming_time_seconds = models.IntegerField(null=True, default=None, blank=True)
    swimming_time_hundredths = models.IntegerField(null=True, default=None, blank=True)
    swimming_did_not_start = models.BooleanField()
    swimming_did_not_finish = models.BooleanField()
    swimming_disqualified = models.BooleanField()
    curling_points = models.IntegerField(null=True, default=None, blank=True)
    curling_did_not_start = models.BooleanField()
    curling_did_not_finish = models.BooleanField()
    curling_disqualified = models.BooleanField()

    def __unicode__(self):
        return '%s %s %s' % (self.startnumber, self.player, self.team)

    class Meta:
        ordering = ('startnumber',)
