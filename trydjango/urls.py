"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from pages.views import home_view,contact_view,about_view
#from blog.views import ArticleListView
#from restaurant.views import item_list
from blog.views import ArticleListView,ArticleDetailView,ArticleCreateView,ArticleUpdateView,ArticleDeletelView
from products.views import dynamic_look_up,product_list_view
from courses.views import CourseListView, CourseCreateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    #path('products/<int:id>', dynamic_lookup_view,name='product'),
    #path('',home_view, name='home'),
    path('accounts/', include('allauth.urls')),
    path('', include('restaurant.urls', namespace='restaurant')),
    #path('courses/', include('courses.urls')),
    #path('', ArticleListView.as_view(), name='article-list'),
    #path('courses/', my_fbv, name='my-fbv'),
    #path('', CourseListView.as_View(template_name='contact.html'), name='course-list'),
    #path('<int:id>', CourseListView.as_View(), name='course-detail'),
    #path('create/ ', CourseCreateView.as_View(), name='course-create'),
    path('<int:id>/', ArticleDetailView.as_view(), name='article-detail'),
    path('<int:id>/delete/', ArticleDeletelView.as_view(), name='article-delete'),
    path('createform/', ArticleCreateView.as_view(), name='article-create'),
    path('<int:id>/update/', ArticleUpdateView.as_view(), name='article-update'),
    
    #path('blog/', include('blog.urls')),
    path('admin/', admin.site.urls),
    path('', include('products.urls')),
    #path('products/<int:my_id>/', product_list_view),
    
    #path('contact/',contact_view),
    #path('itemlist/',item_list),
    #path('product/',product_detail_view),
    #path('create/',product_create_view),
    #ath('list/',product_list_view),
    #path ('k', ArticleListView.as_view(), name='article-list'),
    #path('blog/', include('blog.urls')),
   
    #ath('about/',about_view),
       
]
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
urlpatterns += static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,
                        document_root=settings.STATIC_ROOT)