from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import( TemplateView, ListView,
                                  DetailView, CreateView,
                                  UpdateView, DeleteView)


# Create your views here.
def index(request):
    texto={'mensaje_texto':'Este es mi primer mensaje :)'}
    return render(request, 'index.html', {})

def blog_index(request):
    post_list = Post.objects.all().order_by('-created_on')
    context = {
        "posts": post_list,
    }
    return render(request, "blog_index.html", context)


def blog_detail(request, id):
    post = Post.objects.get(id=id)

    form=CommentForm()
    if request.method=='POST':
        form = CommentForm(request.POST)
        if form.isvalid():
            print("Validacion exitosa!")
            print("Autor:" + form.cleaned_data["author"])
            print("Comentario:" + form.cleaned_data["comment_body"])
            comment = Comment(
                author=form.cleaned_data["author"],
                comment_body=form.cleaned_data["comment_body"],
                post=post
            )
            comment.save()

    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }

    return render(request, 'blog_detail.html', context)


class CreatePostView(CreateView, LoginRequiredMixin):
    login_url= '/login'
    #redirect_field_name='index_detail.html'

    form_class = PostForm

    model = Post








def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )
    context = {
        "category": category,
        "posts": posts
    }
    return render(request, "blog_category.html", context)


@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)


@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/comment_form.html', {'form': form})


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail', pk=post_pk)







def contact(request):
    #return HttpResponse("Hola estoy en la pagina de contacto")
    return render(request, 'index copy.html',{})