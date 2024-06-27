from django.urls import path
from flowers.views import FlowersListView, add_flower, edit_flower, delete_flower
urlpatterns  = [
    path("", FlowersListView.as_view(), name="flowers"),
    path('add/', add_flower, name='add_flower'),
    path('edit/<int:flower_id>/', edit_flower, name='edit_flower'),
    path('delete/<int:flower_id>/', delete_flower, name='delete_flower')
                ]