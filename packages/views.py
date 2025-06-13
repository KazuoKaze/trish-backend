from django.shortcuts import render

# Create your views here.
from .models import Packages, CollegePartners, IndustryPartners, Enquiry, Trip, Blog, BlogTag, MemoryVideo, HomeVideo
from rest_framework.response import Response
from .serializers import PackagesSerializer, CollegePartnerSerializer, IndustryPartnerSerializer, EnquirySerializer, TripSerializer, BlogListSerializer, BlogDetailSerializer, EmailHereSerializer, MemoryVideoSerializer, HomeVideoSerializer
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(["GET"])
def get_packages(request):
    packages = Packages.objects.all()
    serializer = PackagesSerializer(packages, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_college_partners(request):
    partners = CollegePartners.objects.all()
    serializer = CollegePartnerSerializer(partners, many=True, context={'request': request})
    return Response(serializer.data)


@api_view(['GET'])
def get_industry_partners(request):
    partners = IndustryPartners.objects.all()
    serializer = IndustryPartnerSerializer(partners, many=True, context={'request': request})
    return Response(serializer.data)


@api_view(['GET'])
def get_trips(request):
    partners = Trip.objects.all()
    serializer = TripSerializer(partners, many=True, context={'request': request})
    return Response(serializer.data)


@api_view(['POST'])
def submit_enquiry(request):
    serializer = EnquirySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Enquiry submitted successfully!'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





@api_view(['GET'])
def get_all_blogs(request):
    blogs = Blog.objects.filter(is_published=True)
    serializer = BlogListSerializer(blogs, many=True, context={'request': request})
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_single_blog(request, slug):
    try:
        blog = Blog.objects.get(slug=slug, is_published=True)
    except Blog.DoesNotExist:
        return Response({'detail': 'Blog not found.'}, status=status.HTTP_404_NOT_FOUND)

    serializer = BlogDetailSerializer(blog, context={'request': request})
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def subscribe_email(request):
    serializer = EmailHereSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Subscribed successfully.'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_memory_videos(request):
    videos = MemoryVideo.objects.all()
    serializer = MemoryVideoSerializer(videos, many=True, context={'request': request})
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_home_videos(request):
    videos = HomeVideo.objects.all()
    serializer = HomeVideoSerializer(videos, many=True, context={'request': request})
    return Response(serializer.data, status=status.HTTP_200_OK)