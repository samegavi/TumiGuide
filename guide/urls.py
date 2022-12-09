from django.urls import path

from . import views

app_name = "guide"
urlpatterns = [
    path('', views.index, name='index'),
    path('places/', views.AddPlaceView.as_view(), name='place'),
    path('places/<int:pk>/', views.PlaceDetailView.as_view(), name='place_detail'),
    path('places/<int:pk>/edit', views.PlaceUpdateView.as_view(), name='place_update'),
    path('places/index/', views.PlaceListView.as_view(), name='place_index'),
    path('places/<int:pk>/delete/', views.PlaceDeleteView.as_view(), name='place_delete'),
    path('topics/', views.AddTopicView.as_view(), name='topic'),
    path('topics/<int:pk>/', views.TopicDetailView.as_view(), name='topic_detail'),
    path('topics/<int:pk>/edit', views.TopicUpdateView.as_view(), name='topic_update'),
    path('topics/index/', views.TopicListView.as_view(), name='topic_index'),
    path('topics/<int:pk>/delete/', views.TopicDeleteView.as_view(), name='topic_delete'),
    path('entries/', views.AddEntryView.as_view(), name='entry'),
    path('entries/<int:pk>/', views.EntryDetailView.as_view(), name='entry_detail'),
    path('entries/<int:pk>/edit', views.EntryUpdateView.as_view(), name='entry_update'),
    path('entries/index/', views.EntryListView.as_view(), name='entry_index'),
    path('entries/<int:pk>/delete/', views.EntryDeleteView.as_view(), name='entry_delete'),
]