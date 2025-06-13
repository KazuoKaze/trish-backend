from django.db import models
import uuid
from ckeditor.fields import RichTextField
from django.utils.text import slugify

# Create your models here.

class BaseModel(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    class Meta:
        abstract = True

class HighLight(BaseModel):
    name = models.CharField(max_length=2555, blank=False, null=False)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Highlights'

class Packages(BaseModel):
    image = models.ImageField(upload_to='packages/')
    title = models.CharField(max_length=255)
    description = models.TextField()
    days = models.IntegerField(default=0)

    origin = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)

    highlights = models.ManyToManyField(HighLight, blank=True)

    pdf_file = models.FileField(upload_to='packages/pdfs/', blank=True, null=True)
    video_file = models.FileField(upload_to='packages/videos/', blank=True, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Packages'


class CollegePartners(BaseModel):
    image = models.ImageField(upload_to='college/')
    title = models.CharField(max_length=255)
    description = models.TextField()
    highlights = models.CharField(max_length=255)
    col_num = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'College-Partners'


class IndustryPartners(BaseModel):
    image = models.ImageField(upload_to='industry/')
    title = models.CharField(max_length=255)
    description = models.TextField()
    hq = models.CharField(max_length=255)
    highlight = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Industry-Partners'


class Enquiry(BaseModel):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    college = models.CharField(max_length=255, blank=True)
    course = models.CharField(max_length=255, blank=True)
    package = models.CharField(max_length=255)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.package}"
    
class Trip(BaseModel):
    image = models.ImageField(upload_to='trip/')
    title = models.CharField(max_length=255)
    place_name = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Trip-Highlights'


class Author(BaseModel):
    image = models.ImageField(upload_to='author/')
    name = models.CharField(max_length=255)
    sub_heading = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Authors'


class BlogTag(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Blog-Tags'



# Main Blog model
class Blog(BaseModel):
    highlight = models.CharField(max_length=255)
    image = models.ImageField(upload_to='blog/')
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True, max_length=255)
    sub_heading = models.TextField()
    min_read = models.IntegerField()
    blog_tags = models.ManyToManyField(BlogTag)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    is_published = models.BooleanField(default=True)
    content = RichTextField()
    related_blogs = models.ManyToManyField("self", blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            raw_slug = slugify(self.title)
            if len(raw_slug) > 255:
                # Cut at the last dash before 255 chars
                raw_slug = raw_slug[:255]
                last_dash = raw_slug.rfind('-')
                if last_dash > 0:
                    raw_slug = raw_slug[:last_dash]
            self.slug = raw_slug
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Blogs'


class EmailHere(BaseModel):
    email = models.CharField(max_length=2555)

    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name_plural = 'User-Emails'


class MemoryVideo(BaseModel):
    video = models.FileField(upload_to='memory_videos/')
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Memory Video {self.uuid}"
    
    class Meta:
        verbose_name_plural = 'Memory-Videos'

class HomeVideo(BaseModel):
    video = models.FileField(upload_to='home_videos/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Home Video {self.uuid}"
    
    class Meta:
        verbose_name_plural = 'Home-Videos'

