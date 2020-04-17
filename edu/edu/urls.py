from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('ecenter.urls')),
    path('blog/', include('blog.urls')),
    path('profile/', include('users.urls')),
    path('about/', include('about.urls')),
    path('contact/', include('contact.urls')),
    path('courses/', include('courses.urls'))
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.site.site_header = "EduCenter"
admin.site.site_title = "EduCenter"
admin.site.site_index_title = "Welcome To EduCenter"