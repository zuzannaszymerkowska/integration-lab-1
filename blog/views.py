from django.views.generic import ListView, DetailView
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html' # ścieżka do szablonu
    context_object_name = 'posts'         # nazwa zmiennej w HTML

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

from django.http import JsonResponse
from .models import Post

def api_posts(request):
    posts = list(Post.objects.all().values('id', 'title', 'content'))
    return JsonResponse(posts, safe=False)