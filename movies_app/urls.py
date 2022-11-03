from django.urls import path, include
from rest_framework.routers import DefaultRouter

# from movies_app.models import Watchlist
from .views import  UserDataView, MarriageView, ChildView

# router = DefaultRouter()
# router.register('stream', StreamPlatformsViewSet, basename='streamplatform')

urlpatterns = [
    # path('list/', WatchListView.as_view(), name = 'movie_list'),
    # path('list/<int:pk>', WatchDetail.as_view(), name = 'movie_main'),
    # path('newlist/', WatchListGV.as_view(), name = 'movie_watchlist'),

    # path('', include(router.urls)),

    # path('details/', StreamPlatformsList.as_view(), name ='streams'),
    # path('details/<int:pk>', StreamPlatformsDetail.as_view(), name = 'stream_detail'),
    # path('reviews/', ReviewList.as_view(), name = 'review-list'),
    # path('reviews/<int:pk>', ReviewDetail.as_view(), name ='review-detail'),
    # path('details/<int:pk>/reviews-create/', ReviewCreate.as_view(), name ='review-create'),
    # path('details/<int:pk>/reviews/', ReviewList.as_view(), name='review-list'),
    # path('details/reviews/<int:pk>', ReviewDetail.as_view(), name ='review-datail'),
     path('createmale/', UserDataView.as_view()),
     path('Marriage/', MarriageView.as_view()),
     path('Child/', ChildView.as_view()),
]

