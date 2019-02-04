from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.HomeListView.as_view(), name='home'),
    path('furniture_list/',
        views.FurnitureListView.as_view(),
        name='furniture-list-all',
    ),
    path(
        'piece/<uuid:pk>',
        views.FurnitureDetailView.as_view(),
        name='furniture-detail',
    ),
    path('add_piece/',
        views.FurnitureCreate.as_view(),
        name='add-piece',
    ),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
