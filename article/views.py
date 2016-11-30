from django.shortcuts import render
from article.models import Article
from django.http import HttpResponseRedirect

#home and detail_page
def main_page(request):
	posts = Article.objects.all()
	return render(request,'home.html',{'post_list':posts})

def detail(request, id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'detail.html', {'post' : post})

#addpost
def addpost(request):
	return render(request,'addpost.html') 

def blog_add(request):
	content = request.POST.get('content')        
	title = request.POST.get('title')
	tag = request.POST.get('tags')                   
	blog = Article.objects.create(title=title,category=tag,content=content,)
	id = Article.objects.order_by('-date_time')[0].id
	return HttpResponseRedirect('/%s' %id)


from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
def index(request):                                                            
	posts = Article.objects.all().order_by('-date_time')                                              
	paginator = Paginator(posts,3)                                               #每页显示3篇blog进行分页                                         
	page = request.GET.get('page',1)                                           #获取当前页的数字
	try: 
	    current_page = paginator.page(page)                                      #获取当前页
	except PageNotAnInteger:                                                     #如果系统从0开始，就赋初值为1
		current_page = paginator.page(1)                                         
	blog_list = current_page.object_list                                        
	return render(request,'home.html',{'post_list':blog_list,'current_page':current_page}) 