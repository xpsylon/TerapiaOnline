"""
URL configuration for TerapiaOnline project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
#estas dos proximas lineas son para servir media files...chequear linea + static ...
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace='main')),
    #Getting the Django pre-built auth urls:
    path('', include('django.contrib.auth.urls')),
    path('', include('users.urls', namespace='users')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('', include('therapists.urls', namespace='therapists'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""
URL Configuration for the Django project.

The `urlpatterns` list routes URLs to views. For more information, please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/

This configuration includes several URL patterns:

- The admin site is available at '/admin/'.
- The 'main' app's URLs are included at the root path ('/').
- Django's built-in authentication views (login, logout, password change, etc.) are also included at the root path.
- The 'users' app's URLs are included at the root path.
- The 'blog' app's URLs are included at '/blog/'.

Each included URL configuration is associated with a namespace:
- 'main' for the 'main' app.
- 'users' for the 'users' app.
- 'blog' for the 'blog' app.

Namespaces allow you to reverse URLs for included URL configurations. For example, you can use `reverse('blog:post_detail', args=[post_id])` to get the URL for a specific blog post.
"""
