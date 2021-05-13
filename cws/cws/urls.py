"""cws URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, re_path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from ckeditor_uploader import urls as ck_urls
from rest_framework import routers
import rest_framework.urls
from mainapp.views import Home, ContentCardViewSet, EducationListView
from questionapp.views import QuestionViewSet,  question_page, TestListView
from mainapp.api.views import CommentList, CommentDetail

router =  routers.DefaultRouter()
router.register(r'question/(?P<id>.+)', QuestionViewSet)
router.register('content_card', ContentCardViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name="Home"),
    path('api/',include(router.urls)),
    path('question/', include('questionapp.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='mainapp/login.html'),name="login"),
    path('ckeditor/', include(ck_urls)),
    path('edu/<int:id>/', EducationListView.as_view(), name="Education"),
    path('test/', TestListView.as_view(), name='TestList'),
    path('test/<int:id>/', question_page, name='question_page'),
    path('api-auth/', include('rest_framework.urls')),
    path('comments/', CommentList.as_view()),
    path('comments/<int:pk>/', CommentDetail.as_view()),
 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  
