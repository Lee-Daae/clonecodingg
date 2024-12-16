
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.forms import ValidationError
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView

from articleapp.models import Article
from likeapp.models import Like

@transaction.atomic
def db_transaction(user, article):

    article.like += 1
    article.save()

    if Like.objects.filter(user=user, article=article).exists():
        raise ValidationError('Like already exists')
    else:
        Like(user=user, article=article).save()
    


@method_decorator(login_required, name='get')
class LikeArticleView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('articleapp:detail', kwargs={'pk':kwargs['pk']})
    
    def get(self, *args, **kwargs):

        user = self.request.user
        article = get_object_or_404(Article, pk=kwargs['pk'])
        try:
            db_transaction(user, article)
            messages.add_message(self.request, messages.SUCCESS, '좋아요 반영')
        except ValidationError:
            messages.add_message(self.request, messages.ERROR, '좋아요 한번가능')
            return HttpResponseRedirect(reverse('articleapp:detail', kwargs={'pk': kwargs['pk']}))
            

        return super(LikeArticleView, self).get(self.request, *args, **kwargs)
    