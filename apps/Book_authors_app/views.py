from django.shortcuts import render
from .models import Blog
# Create your views here.
def index(req):
  return render(req, 'Book_authors_app/index.html')

# from django.shortcuts import render
# from .models import Blog

# def update(request):
#   errors = Blog.objects.basic_validator(request.POST)
#       if len(errors):
#          for tag, error in errors.iteritems():
#               messages.error(request,error,extra_tags =tag)
#         return redirect('/blog/edit/' +id)
#       else:
#           blog = Blog.objects.get(id =id)
#           blog.name = request.POST['name']
#           blog.desc = request.POST['desc']
#           blog.save()
#           return redirect('/blogs')