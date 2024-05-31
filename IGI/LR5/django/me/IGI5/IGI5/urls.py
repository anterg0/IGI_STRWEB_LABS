"""
URL configuration for IGI5 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from IGI import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('faq', views.faq, name='faq'),
    path('codeofcond', views.coc, name='code'),
    path('news', views.news, name='news'),
    path('news/<int:pk>', views.NewsDetailView.as_view(), name='news-detail'),
    path('news/<int:pk>/edit', views.NewsUpdateView.as_view(), name='news-edit'),
    path('news/<int:pk>/delete', views.NewsDeleteView.as_view(), name='news-delete'),
    path('news/create', views.create_article, name='create-article'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('api', views.api_view, name='api'),
    path('profile', views.profile, name='profile'),
    path('promos', views.promo_view, name='promocodes'),
    path('register', views.register_view, name='register'),
    path('jobs', views.jobs, name='jobs'),
    path('jobs/create', views.create_job, name='job-create')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
