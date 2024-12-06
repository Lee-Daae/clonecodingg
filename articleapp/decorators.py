from django.http import HttpResponseForbidden

from articleapp.models import Article


def article_owner_required(func): 
    def decorated(request, *args, **kwargs): 
        article = Article.objects.get(pk=kwargs['pk'])
        if not article.writer == request.user:
            return HttpResponseForbidden()   # 금지 되었다고 내보내기
        return func(request, *args, **kwargs) # 같다면 그냥 보내주기
    return decorated