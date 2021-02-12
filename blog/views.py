from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.urls import reverse
from django.contrib import messages
from .models import Post,Comment, Contact
# Create your views here.

class HomeView(generic.ListView):
	template_name = 'blog/home.html'
	model = Post
	context_object_name = 'posts'
	
    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get a context
    #     context = super().get_context_data(**kwargs)
    #     # Add in a QuerySet of all the books
    #     context['title'] = "&C"
    #     return context

def detailview(request,post_id):
    post = get_object_or_404(Post,pk=post_id)
    comments = post.comment_set.all().order_by("-date_posted")

    context = {
        "post":post,
        "comments":comments
    }
    return render(request,'blog/detail.html',context)

def commentview(request,post_id):
    post = get_object_or_404(Post,pk=post_id)
    content = request.POST["comment"]
    author = request.user
    the_comment = Comment.objects.create(
        content=content,
        post=post,
        author=author
        )
    the_comment.save()
    return HttpResponseRedirect(reverse('blog:post_detail', args=([post.id])))

def aboutmeview(request):
    if request.method == "POST":
        message = request.POST['message']
        email = request.POST['email']
        subject = request.POST['subject']

        # send_mail(
        #     subject,
        #     message+"\n Sender's email: "+email,
        #     'elijahokellp@gmail.com',
        #     ['elijahokello90@gmail.com'],
        #     fail_silently=False,
        #     )
        contact = Contact.objects.create(email=email,message=message,subject=subject)
        contact.save()
        messages.success(request, f'Your message has been received successfully')
        return HttpResponseRedirect(reverse('blog:aboutme'))
    else:
        return render(request,'blog/about_me.html')