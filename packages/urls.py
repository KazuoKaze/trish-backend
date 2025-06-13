from django.urls import path
from .views import get_packages, get_college_partners, get_industry_partners, submit_enquiry, get_trips, get_all_blogs, get_single_blog, subscribe_email, get_memory_videos, get_home_videos

urlpatterns = [
    path('packages/', get_packages, name='get-packages'),
    path('get_college_partners/', get_college_partners, name='get_college_partners'),
    path('get_industry_partners/', get_industry_partners, name='get_industry_partners'),
    path('get_trips/', get_trips, name='get_trips'),
    path('submit-enquiry/', submit_enquiry, name='submit-enquiry'),
    path('blogs/', get_all_blogs, name='get_all_blogs'),
    path('blogs/<slug:slug>/', get_single_blog, name='get_single_blog'),
    path('subscribe_email/', subscribe_email, name='subscribe_email'),
    path('get_memory_videos/', get_memory_videos, name='get_memory_videos'),
    path('get_home_videos/', get_home_videos, name='get_home_videos'),
]