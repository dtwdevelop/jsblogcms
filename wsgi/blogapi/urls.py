from rest_framework.routers import DefaultRouter
from . import views
router = DefaultRouter()
router.register(r'categories', views.CategoryViewSet)
router.register(r'pages', views.PagesViewSet)
router.register(r'comments', views.CommentsViewSet)

