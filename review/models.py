from django.db import models

class Review(models.Model):
  TEAM_CHOICES = (
    ('H1', 'Heren'),
    ('D1', 'Dames1'),
    ('D2', 'Dames2'),
  )

  home = models.CharField('Thuis', max_length=50)
  visitor = models.CharField('Bezoekers', max_length=50)
  points_home = models.IntegerField('Punten thuis')
  points_visitor = models.IntegerField('Punten bezoekers')
  body = models.TextField('Beschrijving')
  team = models.CharField('Ploeg', max_length=2, choices=TEAM_CHOICES)
  match_date = models.DateField('match datum')

  def __unicode__(self):
    return self.home + " - " + self.visitor
