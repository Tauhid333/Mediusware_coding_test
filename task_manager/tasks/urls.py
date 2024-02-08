from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.sys_login, name='login'),
    path('logout/', views.sys_logout, name='logout'),
    path('home/', views.home, name='home'),

    # Task
	path('task/', views.task_list, name='task_list'),
	path('task/edit/<int:id>/', views.task_update, name='task_update'),
	path('task/delete/<int:id>/', views.task_delete, name='task_delete'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)