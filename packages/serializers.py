from rest_framework import serializers
from .models import Packages, HighLight, CollegePartners, IndustryPartners, Enquiry, Trip, BlogTag, Blog, Author, EmailHere, MemoryVideo, HomeVideo

class HighLightSerializer(serializers.ModelSerializer):
    class Meta:
        model = HighLight
        fields = ['uuid', 'name']

class PackagesSerializer(serializers.ModelSerializer):
    highlights = HighLightSerializer(many=True)

    class Meta:
        model = Packages
        fields = [
            'uuid',
            'title',
            'description',
            'image',
            'days',
            'origin',
            'destination',
            'highlights',
            'pdf_file',   # or 'pdf_url' if you're using URLField
            'video_file', # or 'video_url'
        ]


class CollegePartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollegePartners
        fields = ['uuid', 'image', 'title', 'description', 'highlights', 'col_num']


class IndustryPartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndustryPartners
        fields = ['uuid', 'image', 'title', 'description', 'hq', 'highlight']

class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ['uuid', 'image', 'title', 'place_name']


class EnquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Enquiry
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name', 'sub_heading', 'image']






class BlogTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogTag
        fields = ['name']


class BlogListSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    blog_tags = BlogTagSerializer(many=True)

    class Meta:
        model = Blog
        fields = ['title', 'slug', 'image', 'highlight', 'min_read', 'author', 'blog_tags', 'is_published']
        

class BlogDetailSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    blog_tags = BlogTagSerializer(many=True)
    related_blogs = BlogListSerializer(many=True)

    class Meta:
        model = Blog
        fields = ['title', 'slug', 'image', 'highlight', 'sub_heading', 'min_read', 'author', 'blog_tags', 'content', 'related_blogs']



class EmailHereSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailHere
        fields = ['email']


class MemoryVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemoryVideo
        fields = ['uuid', 'video', 'title', 'description']


class HomeVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeVideo
        fields = ['uuid', 'video']