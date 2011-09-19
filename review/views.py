from django.template import Context, loader
from review.models import Review
from django.http import HttpResponse

def index(request):
    latest_review_list = Review.objects.all().order_by('-match_date')[:5]
    t = loader.get_template('review/index.html')
    c = Context({
        'latest_review_list': latest_review_list,
    })
    return HttpResponse(t.render(c))
