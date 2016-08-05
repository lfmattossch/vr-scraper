from django.http import HttpResponse
from django.template import loader

from scrapper.models import Article


def index(request):
    latest_article_list = Article.objects.order_by('-publication_date')[:10]
    template = loader.get_template('scrapper/template.html')
    context = {
        'articles': latest_article_list.values(
        	'title', 'publication_date', 'author__name', 'content'
        )
    }
    return HttpResponse(template.render(context, request))