from django.urls import path, include
from rest_framework_nested import routers
from .views import NoteViewSet, NoteItemViewSet

router = routers.SimpleRouter()
router.register(r'', NoteViewSet)

nested_router = routers.NestedSimpleRouter(
    router, r'', lookup='note')
nested_router.register(
    r'note-items', NoteItemViewSet)

urlpatterns = [
    path(r'', include(router.urls)),
    path(r'', include(nested_router.urls)),
]
