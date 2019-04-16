from django.shortcuts import render, HttpResponse, redirect
from .models import Show
from django.db.models import Q
import datetime

def index(request):
    return redirect("/shows")

# ('/users')  url(r'^shows$', views.all_shows),     
def all_shows(request):
	context = { "all_shows": Show.objects.all() }
	return render(request, "tv/index.html", context)
    
# ("/users/<user_id>") url(r'^shows/(?P<show_id>\d+)$', views.display_show),      
def display_show(request, show_id):
    this_show=Show.objects.get(id=show_id)
    context = { "show" : this_show }
    return render(request, "tv/show_show.html", context)

# ("/users/new") url(r'^shows/new$', views.new_show),
def new_show(request):
    return render(request, "tv/add_show.html")

# ("/users/create", methods=["POST"])  url(r'^shows/create$', views.create_show),
def create_show(request):     
    is_valid=True     
    context = { 'error_msgs' : [] }
    if len(request.POST['title']) < 1:
        is_valid=False
        context['error_msgs'].append("Title cannot be blank")
    if len(request.POST['network']) < 1:
        is_valid=False
        context['error_msgs'].append("Network cannot be blank")
    if len(request.POST['rel_date']) < 1:
        is_valid=False
        context['error_msgs'].append("Release Date cannot be blank")
    if len(request.POST['desc']) < 1:
        is_valid=False
        context['error_msgs'].append("Description cannot be blank")
    if is_valid:
        req_title=request.POST['title']
        req_network=request.POST['network']
        req_rel_date = datetime.datetime.strptime(request.POST['rel_date'], '%Y-%m-%d')
        req_desc=request.POST['desc']
        new_show=Show.objects.create(title=req_title, network=req_network, \
                release_date=req_rel_date, description=req_desc)
        if not new_show:
            is_valid=False
            context['error_msgs'].append("Could not add this TV Show")
    if is_valid:
        return redirect(f"/shows/{new_show.id}")
    else:
        return render(request, "tv/add_show.html", context)

# ("/users/<user_id>/edit") url(r'^users/(?P<id>\d+)/edit$', views.edit_show),
def edit_show(request, show_id):         
    this_show=Show.objects.get(id=show_id)
    context = { 
        "show" : this_show,
        "time" : this_show.release_date.strftime('%Y-%m-%d') 
    }
    return render(request, "tv/edit_show.html", context)

# ("/users/<user_id>/update", methods=["POST"]) url(r'^users/(?P<id>\d+)/update$', views.update_show),         
def update_show(request, show_id):       
    is_valid=True     
    context = { 'error_msgs' : [] }
    if len(request.POST['title']) < 1:
        is_valid=False
        context['error_msgs'].append("Title cannot be blank")
    if len(request.POST['network']) < 1:
        is_valid=False
        context['error_msgs'].append("Network cannot be blank")
    if len(request.POST['rel_date']) < 1:
        is_valid=False
        context['error_msgs'].append("Release Date cannot be blank")
    if len(request.POST['desc']) < 1:
        is_valid=False
        context['error_msgs'].append("Description cannot be blank")
    if is_valid:
        this_show=Show.objects.get(id=show_id)
        this_show.title=request.POST['title']
        this_show.network=request.POST['network']
        this_show.release_date=datetime.datetime.strptime(request.POST['rel_date'], '%Y-%m-%d')
        this_show.description=request.POST['desc']
        success=this_show.save()  
        return redirect("/shows/" + show_id)
    else:
        return render(request, "tv/edit_show.html", context)

# ("/users/<user_id>/destroy") url(r'^users/(?P<id>\d+)/destroy$', views.delete_show),
def delete_show(request, show_id):       
    this_show=Show.objects.get(id=show_id)
    success=this_show.delete()
    return redirect("/shows")

