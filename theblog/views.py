from django.shortcuts import render, get_object_or_404
from django.urls.base import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from  .models import Category, Post, Comment
from .forms import PostForm, EditForm, CommentForm
from django.http  import HttpResponseRedirect

# Create your views here.

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
        liked = True
    
    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))

#def home(request):
#   return render(request, 'home.html', {}) 
class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    #ordering = ['-id']
#order by negetive date
    ordering =['-post_date']

    def get_context_data(self, *args, **kwargs):
       cat_menu = Category.objects.all()
       context = super(HomeView, self).get_context_data(*args, **kwargs)
       context["cat_menu"] = cat_menu
       return context

def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-', ' '))
    return render (request, 'category.html', {'cats':cats.title().replace('-', ' '), 'category_posts': category_posts })

def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render (request, 'category_list.html', {'cat_menu_list':cat_menu_list})

class ArticleDetailView(DetailView):
    model = Post
    template_name = "article_detail.html"

    def get_context_data(self, *args, **kwargs):
       cat_menu = Category.objects.all()
       context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
       cur = get_object_or_404(Post, id=self.kwargs['pk'])
       context["cat_menu"] = cat_menu
       total_likes = cur.total_likes()
       liked = False
       if cur.likes.filter(id=self.request.user.id).exists():
         liked = True
       context["total_likes"] = total_likes
       context["liked"] = liked
       return context

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    #fields = '__all__'


class AddCategoryView(CreateView):
    model = Category
    #form_class = PostForm
    template_name = 'add_category.html'
    fields = '__all__'


class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    #fields = ['title', 'title_tag', 'body']


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post=post)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user  # Assuming you have user authentication
            comment.save()
    else:
        form = CommentForm()

    return render(request, 'article_detail.html', {'post': post, 'comments': comments, 'form': form})