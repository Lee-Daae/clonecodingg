
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView

from articleapp.models import Article
from likeapp.models import Like

@method_decorator(login_required, name='get')
class LikeArticleView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('articleapp:detail', kwargs={'pk':kwargs['pk']})
    
    def get(self, *args, **kwargs):

        user = self.request.user
        article = get_object_or_404(Article, pk=kwargs['pk'])

        if Like.objects.filter(user=user, article=article).exists():
            messages.add_message(self.request, messages.ERROR, '좋아요 한번가능')
            return HttpResponseRedirect(reverse('articleapp:detail', kwargs={'pk': kwargs['pk']}))
        else:
            Like(user=user, article=article).save()
        
        article.like += 1
        article.save()

        messages.add_message(self.request, messages.SUCCESS, '좋아요 반영')

        return super(LikeArticleView, self).get(self.request, *args, **kwargs)
    