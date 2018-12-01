from django.urls import LOCALE_PATHS
from .views import PostList, PostDetail

urlpatterns = [
path('', PostList.as_view()),
path('<int>:pk/', PostDetail.as_view()),
]

