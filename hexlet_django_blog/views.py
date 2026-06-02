from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View


class IndexView(View):
    def get(self, request, *args, **kwargs):
        url = reverse('article', kwargs={'tags': 'python', 'article_id': 42})
        return redirect(url)

def about(request):
    return render(request, 'about.html')
