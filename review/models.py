from django.db import models

class Review(models.Model):
  TEAM_CHOICES = (
    ('H1', 'Heren'),
    ('D1', 'Dames1'),
    ('D2', 'Dames2'),
  )

  title = models.CharField(max_length=100)
  body = models.TextField()
  team = models.CharField(max_length=2, choices=TEAM_CHOICES)
  match_date = models.DateTimeField('date match')
