# -*- coding:utf-8 -*-
from django.shortcuts import render
from core.models import Post, Comment
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.utils import timezone
from django.core.urlresolvers import reverse
# Create your views here.

def index(request):
	post = Post.objects.all().order_by('id')
	return render(request, 'index.html', { 'post' : post })

def cadComment(request):
	post = Post.objects.all().order_by('id')
	if request.method == 'POST':
		id_post = request.POST['id_post']
		p = Post.objects.get(id=id_post)
		name_comment = request.POST['name']
		message_comment = request.POST['comment']
		c = p.comment_set.create(name=name_comment, comment=message_comment, date_publication=timezone.now(), post=id_post)
		c.save()
		return HttpResponseRedirect(reverse('core.views.index', args=('')))
	else:
		return render(request, 'index.html', { 'post' : post })