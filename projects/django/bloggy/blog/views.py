from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.http import HttpResponse
from blog.models import Post
from django.template import Context, loader, RequestContext
from blog.forms import PostForm

# Create your views here.
def index(request):
	latest_posts = Post.objects.all().order_by('-created_at')
	popular_posts=Post.objects.order_by('-views')[:5]

	context_dict={'latest_posts': latest_posts, 'popular_posts':popular_posts,}
	for post in latest_posts:
		post.url=encode_url(post.title)
	for popular_post in popular_posts:
		popular_post.url=encode_url(popular_post.title)

	t=loader.get_template('blog/index.html')
	c=Context(context_dict)
	return HttpResponse(t.render(c))

def encode_url(url):
	return url.replace(' ','_')

def decode_url(url):
	return url.replace('_',' ')

def post(request, post_name):
	single_post=get_object_or_404(Post, title=decode_url(post_name))
	
	t=loader.get_template('blog/post.html')
	c=Context({'single_post':single_post,})
	return HttpResponse(t.render(c))

def add_post(request):
	context = RequestContext(request)
	if request.method=='POST':
		form=PostForm(request.POST, request.FILES)
		if form.is_valid():
			form.save(commit=True)
			return redirect(index)
		else:
			print form.errors
	else:
		form=PostForm()
	return render_to_response('blog/add_post.html',{'form': form}, context)