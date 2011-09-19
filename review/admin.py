from review.models import Review
from django.contrib import admin

class ReviewAdmin(admin.ModelAdmin):
      fields = ['match_date', 'title']

admin.site.register(Review)
