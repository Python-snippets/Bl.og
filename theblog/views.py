from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from  .models import Category, Post
from .forms import PostForm, EditForm

# Create your views here.

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



class ArticleDetailView(DetailView):
    model = Post
    template_name = "article_detail.html"
    def get_context_data(self, *args, **kwargs):
       cat_menu = Category.objects.all()
       context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
       context["cat_menu"] = cat_menu
       return context

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    #fields = '__all__'
    def get_context_data(self, *args, **kwargs):
       cat_menu = Category.objects.all()
       context = super(AddPostView, self).get_context_data(*args, **kwargs)
       context["cat_menu"] = cat_menu
       return context

class AddCategoryView(CreateView):
    model = Category
    #form_class = PostForm
    template_name = 'add_category.html'
    fields = '__all__'
    def get_context_data(self, *args, **kwargs):
       cat_menu = Category.objects.all()
       context = super(AddCategoryView, self).get_context_data(*args, **kwargs)
       context["cat_menu"] = cat_menu
       return context

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    #fields = ['title', 'title_tag', 'body']
    def get_context_data(self, *args, **kwargs):
       cat_menu = Category.objects.all()
       context = super(UpdatePostView, self).get_context_data(*args, **kwargs)
       context["cat_menu"] = cat_menu
       return context

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
    def get_context_data(self, *args, **kwargs):
       cat_menu = Category.objects.all()
       context = super(DeletePostView, self).get_context_data(*args, **kwargs)
       context["cat_menu"] = cat_menu
       return context
