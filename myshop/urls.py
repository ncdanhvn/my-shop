from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "My Shop Admin"
admin.site.index_title = "Admin"

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),
    path('shop/', include('shop.urls')),
]
