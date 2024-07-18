from django.shortcuts import render,redirect,reverse
from django.contrib import messages
from publication.models import *
from .forms import *
from datetime import datetime
from .models import *
from django.urls import reverse

# Create your views here.
def home(request):
    return render(request,'home.html')

def handleblog(request):
    posts=Blogs.objects.all()
    context={"posts":posts}
    return render(request,'handleblog.html',context)

def profile(request):
    profile = Profile.objects.get(id=1)
    context = {
        'profile':profile
    }
    return render(request,'basic.html',context)

def detail(request,id_publication):
    post = Blogs.objects.get(id=id_publication)
    #print("L'identité de l'article est: ",id_publication)
    category=post.category
    publications_en_relation = Blogs.objects.filter(category=category)[:6]
   # num_comments = Comment.objects.all().count()
    num_comments = Comment.objects.filter(commentaire=post).count()
    return render(request,'detail.html',{"post":post,"per":publications_en_relation,"num_comments":num_comments})

def search(request):
    query=request.GET["publication"]
    liste_publication = Blogs.objects.filter(title__icontains=query)
    return render(request,"search.html",{"liste_publication":liste_publication})

def about(request, *args, **kwargs):
    about = About.objects.get(id=1)
    context = {
        'about':about
    }
    return render(request,'about.html',context)

def add_comment(request, pk):
    post = Blogs.objects.get(id=pk)

    form = CommentForm(instance=post)

    if request.method =='POST':
        form = CommentForm(request.POST,instance=post)
        if form.is_valid():
            name = request.user.username
            body = form.cleaned_data['comment_body'];
            c = Comment(commentaire=post,commenter_name=name, comment_body=body,date_added=datetime.now())
            c.save()
            return redirect('/blog')
        else:
            print('form is valid')
    else:
        form=CommentForm()

    context= {
        'form': form
    }

    return render(request,'add_comment.html',context)

def delete_comment(request,pk):
    comment = Comment.objects.filter(commentaire=pk).last()
    commentaire_id = comment.commentaire.id
    comment.delete()
    return redirect('/blog')
    #context = {"posts": comment}
    #return render(request,'detail.html',context)
   # return redirect(reverse('/blog', args=[commentaire_id]))
    #url= reverse('handleblog', kwargs={'pk':pk})
   # return redirect(url)



"""def internshipdetails(request):

    if not request.user.is_authenticated:
        messages.warning(request,"Please login to access this page")
        return redirect("/auth/login/")

    if request.method=="POST":
        fname=request.POST.get('name')
        femail=request.POST.get('email')
        fusn=request.POST.get('usn')
        fcollege=request.POST.get('cname')
        foffer=request.POST.get('offer')
        fstartdate=request.POST.get('startdate')
        fenddate=request.POST.get('enddate')
        fprojreport=request.POST.get('projreport')

# converting to upper case
        fname=fname.upper()
        fusn=fusn.upper()
        fcollege=fcollege.upper()
        fprojreport=fprojreport.upper()
        foffer=foffer.upper() 

        # 
        check1=Internship.objects.filter(usn=fusn)
        check2=Internship.objects.filter(email=femail)

        if check1 or check2:
            messages.warning(request,"Your Details are Stored Already")
            return redirect("/internshipdetails")
        



        query=Internship(fullname=fname,usn=fusn,email=femail,college_name=fcollege,offer_status=foffer,start_date=fstartdate,end_date=fenddate,proj_report=fprojreport)
        query.save()

        messages.success(request,"Form is Submitted Successful!")
        return redirect('/internshipdetails')

    return render(request,'intern.html')"""

def contact(request):
    if request.method=="POST":
        fname=request.POST.get('name')
        femail=request.POST.get('email')
        fphoneno=request.POST.get('num')
        fdesc=request.POST.get('desc')
        query=Contact(name=fname,email=femail,phonenumber=fphoneno,description=fdesc)
        query.save()
        messages.success(request,"Thanks for contacting us. We will get by you Soon!")

        return redirect('/contact')

    return render(request,'contact.html')