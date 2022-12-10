from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import Place, Topic, Entry
from .forms import PlaceForm, TopicForm, EntryForm
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import DetailView, ListView
from django.urls import reverse_lazy, reverse
from django.contrib.messages.views import SuccessMessageMixin


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class AddPlaceView(SuccessMessageMixin, CreateView):
    model = Place
    form_class = PlaceForm
    template_name = "guide/places.html"
    success_message = "Place was successfully created"

class PlaceDetailView(DetailView):
    model = Place
    template_name = "guide/place_detail.html"

class PlaceUpdateView(SuccessMessageMixin, UpdateView):
    model = Place
    form_class = PlaceForm
    template_name = "guide/place_update.html"
    success_message = "Place was successfully updated"

class PlaceListView(ListView):
    model = Place
    template_name = "guide/place_list.html"

class PlaceDeleteView(SuccessMessageMixin, DeleteView):
    model = Place
    success_url = reverse_lazy("guide:place_index")
    success_message = "Place was successfully destroyed"


#def create_place(request):
    #return HttpResponse("You're looking at a list of places")
    #if request.method == "POST":
        #form = PlaceForm(request.POST) # can be (request.POST or None)
        #if form.is_valid():
            #new_place = form.save() # use .create instead?
            
            #return HttpResponseRedirect(reverse("guide:place_detail", args=[new_place.pk])) #create and add a success page url    
    #else:
        #form = PlaceForm()

    #context = {
        #"form": form
    #}
    #return render(request, "guide/places.html", context)

#def place_detail(request, place_id):
    #try:
        #place = Place.objects.get(pk=place_id)
    #except Place.DoesNotExist:
        #raise Http404("Place does not exist")
    
    #context = {"place": place}

    #return render(request, "guide/place_detail.html", context)


class AddTopicView(SuccessMessageMixin, CreateView):
    model = Topic
    form_class = TopicForm
    template_name = "guide/topics.html"
    success_message = "Topic was successfully created"

class TopicDetailView(DetailView):
    model = Topic
    template_name = "guide/topic_detail.html"

class TopicUpdateView(SuccessMessageMixin, UpdateView):
    model = Topic
    form_class = TopicForm
    template_name = "guide/topic_update.html"
    success_message = "Topic was successfully updated"

class TopicListView(ListView):
    model = Topic
    template_name = "guide/topic_list.html"

class TopicDeleteView(SuccessMessageMixin, DeleteView):
    model = Topic
    success_url = reverse_lazy("guide:topic_index")
    success_message = "Topic was successfully destroyed"
    
    
   

#def entry(request):
    #return HttpResponse("You're looking at table of entries")
    #all_place_objects = Place.objects.all()
    #all_topic_objects = Topic.objects.all()
    
    #context = {
        #"place_object" : all_place_objects,
        #"topic_object" : all_topic_objects
    #}
    #return render(request, "guide/entries.html", context)

class AddEntryView(SuccessMessageMixin, CreateView):
    model = Entry
    form_class = EntryForm
    template_name = "guide/entries.html"
    success_message = "Entry was successfully created"

class EntryDetailView(DetailView):
    model = Entry
    template_name = "guide/entry_detail.html"

class EntryUpdateView(SuccessMessageMixin, UpdateView):
    model = Entry
    form_class = EntryForm
    template_name = "guide/entry_update.html"
    success_message = "Entry was successfully updated"

class EntryListView(ListView):
    model = Entry
    template_name = "guide/entry_list.html"

class EntryDeleteView(SuccessMessageMixin, DeleteView):
    model = Entry
    success_url = reverse_lazy("guide:entry_index")
    success_message = "Entry was successfully destroyed"

