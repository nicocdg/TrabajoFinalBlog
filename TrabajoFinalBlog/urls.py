from pydoc import doc
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include #manually added the include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('WebBlog/', include("WebBlog.urls")) #include the functions from the secondary app urls.py file
]
