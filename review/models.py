from django.db import models

class Review(models.Model):
  TEAM_CHOICES = (
    ('H1', 'Heren'),
    ('D1', 'Dames1'),
    ('D2', 'Dames2'),
    ('V', 'Vets'),
  )

  home = models.CharField('Thuis', max_length=50)
  visitor = models.CharField('Bezoekers', max_length=50)
  points_home = models.IntegerField('Punten thuis')
  points_visitor = models.IntegerField('Punten bezoekers')
  points_q1_home = models.IntegerField('Punten Q1 thuis')
  points_q1_visitor = models.IntegerField('Punten Q1 bezoekers')
  points_q2_home = models.IntegerField('Punten Q2 thuis')
  points_q2_visitor = models.IntegerField('Punten Q2 bezoekers')
  points_q3_home = models.IntegerField('Punten Q3 thuis')
  points_q3_visitor = models.IntegerField('Punten Q3 bezoekers')
  points_q4_home = models.IntegerField('Punten Q4 thuis')
  points_q4_visitor = models.IntegerField('Punten Q4 bezoekers')
  body = models.TextField('Beschrijving')
  team = models.CharField('Ploeg', max_length=2, choices=TEAM_CHOICES)
  match_date = models.DateField('match datum')

  def __unicode__(self):
    return self.home + " - " + self.visitor
