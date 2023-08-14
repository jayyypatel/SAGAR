from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('index/',views.index,name='index'),
    path('join_us_request/',views.join_us_request,name='join_us_request'),
    path('approved_membership/',views.approved_membership,name='approved_membership'),
    path('<int:id>/request_profile/',views.request_profile,name= 'request_profile'),
    path('publications/',views.publications,name='publications'),
    path('add_publications/',views.add_publications,name='add_publications'),
    path('<int:id>/delete_publications',views.delete_publications,name='delete_publications'),
    path('<int:id>/edit_publications/',views.edit_publications,name='edit_publications'),
    path('<int:id>/approve_request/',views.approve_request,name='approve_request'),
    path('<int:id>/delete_request/',views.delete_request,name='delete_request'),
    path('contact_us_request/',views.contact_us_request,name='contact_us_request'), 
    path('<int:id>/delete_contact_request/',views.delete_contact_request,name='delete_contact_request'), 
    path('donate_us_request/',views.donate_us_request,name='donate_us_request'),
    path('<int:id>/donate_receipt/',views.donate_receipt,name='donate_receipt'),
    path('<int:id>/donate_details',views.donate_details,name='donate_details'),
    path('donate_approved/',views.donate_approved,name='donate_approved'),
    path('<int:id>/donate_delete/',views.donate_delete,name='donate_delete')
]
