from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework import routers
from django.urls import include, path

from . import views

app_name = 'services'

router = routers.DefaultRouter()
router.register('library', views.LibraryViewSet, basename='books')

schema_view = SpectacularAPIView.as_view(
    patterns=[path("library/", include("services.urls"))],
)
swagger_view = SpectacularSwaggerView.as_view(
    title="Virtual Library API",
    url_name="library_schema",
)

urlpatterns = [
    path("", include(router.urls)),
    path("docs/", swagger_view, name="services_docs"),
    path("schema/", schema_view, name="library_schema"),
]