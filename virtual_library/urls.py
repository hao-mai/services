from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework import routers
from django.urls import include, path
from django.conf import settings

from virtual_library import viewsets
from virtual_library import views

router = routers.DefaultRouter()
router.register('books', viewsets.BookViewSet, basename='book')
router.register('user', viewsets.UserViewSet, basename='user')
router.register('checkout', viewsets.CheckoutViewSet, basename='checkout')

urlpatterns = [
    path("", include(router.urls)),
]

if settings.DEBUG or settings.ENVIRONMENT == "test":
    schema_view = SpectacularAPIView.as_view(
        patterns=[path("virtual_library/", include("virtual_library.urls"))],
        )
    swagger_view = SpectacularSwaggerView.as_view(
        title="Library API",
        url_name="library_schema",
    )
    urlpatterns += [
        path("docs/", swagger_view, name="library_docs"),
        path("schema/", schema_view, name="library_schema"),
        path('book_view/', views.book_view, name='book_view')
    ]
