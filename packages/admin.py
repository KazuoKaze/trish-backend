from django.contrib import admin

# Register your models here.
from .models import HighLight, Packages, CollegePartners, IndustryPartners, Enquiry, Trip, Author, Blog, BlogTag, EmailHere, MemoryVideo, HomeVideo

from unfold.admin import ModelAdmin

@admin.register(Packages)
@admin.register(CollegePartners)
@admin.register(IndustryPartners)
@admin.register(Enquiry)
@admin.register(Trip)

@admin.register(HighLight)


@admin.register(Author)



@admin.register(BlogTag)



@admin.register(Blog)


@admin.register(EmailHere)

@admin.register(MemoryVideo)

@admin.register(HomeVideo)



class CustomAdminClass(ModelAdmin):
    pass