from django.shortcuts import render
# from rest_framework.decorators import api_view 
from .models import ChildData, User, Marriage
from rest_framework import status
from .serializers import ChildDataSerializer, UserSerializer, MarriageSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
# from rest_framework import mixins
from rest_framework import generics
from rest_framework import filters
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from rest_framework.permissions import BasePermission, IsAuthenticated
from .permission import ReviewUserOrReadOnly, AdminOrReadOnly
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
# from django_filters.rest_framework import DjangoFilterBackend
from .pagination import WatchListPagination
from django.core.mail import EmailMessage
from django.conf import settings

# Create your views here.


##################using viewset################
# class StreamPlatformsViewSet(viewsets.ModelViewSet):
#     queryset = StreamPlatforms.objects.all()
#     serializer_class = StreamPlatformsSerializer
#     permission_classes = [AdminOrReadOnly]

# class StreamPlatformsViewSet(viewsets.ViewSet):

#     def list(self, request):
#         queryset = StreamPlatforms.objects.all()
#         serializer = StreamPlatformsSerializer(queryset, many=True)
#         return Response(serializer.data)
    
#     def retrieve(self, request, pk=None):
#         queryset = StreamPlatforms.objects.all()
#         watchlist = get_object_or_404(queryset, pk=pk)
#         serializer = StreamPlatformsSerializer(watchlist)
#         return Response(serializer.data)

# ###########USING CONCRETE CLASS ############
# class ReviewCreate(generics.CreateAPIView):
#     serializer_class = ReviewSerializer
#     permission_classes = [IsAuthenticated]
#     throttle_classes = [UserRateThrottle, AnonRateThrottle]


#     def get_queryset(self):
#         return Review.objects.all()

        
#     def perform_create(self, serializer):
#        pk = self.kwargs.get('pk')
#        watch = Watchlist.objects.get(pk=pk)

#        review_user = self.request.user
       
#        review_query = Review.objects.filter(Watchlist = watch, review_user=review_user)

#        if review_query.exists():
#         raise ValidationError("You have already reviewed")
    
#        if watch.no_of_rating == 0:
#         watch.avg_rating = serializer.validated_data['rating']
#        else:
#         watch.avg_rating = (watch.avg_rating + serializer.validated_data['rating'])/2
       
#        watch.no_of_rating = watch.no_of_rating + 1
#        watch.save()

#        serializer.save(Watchlist = watch, review_user = review_user)


# class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Review.objects.all()
#     permission_classes = [ReviewUserOrReadOnly]
#     serializer_class = ReviewSerializer
#     throttle_classes = [UserRateThrottle, AnonRateThrottle]


# class ReviewList(generics.ListCreateAPIView):
#     # queryset = Review.objects.all()
#     # permission_classes = [IsAuthenticated]
#     # permission_classes = [ReviewUserOrReadOnly]
#     serializer_class = ReviewSerializer
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['review_user__username', 'active']

#     def get_queryset(self):
#         pk = self.kwargs['pk']
#         return Review.objects.filter(Watchlist=pk)

# class WatchListGV(generics.ListAPIView):
    # queryset = Review.objects.all()
    # permission_classes = [IsAuthenticated]
    # permission_classes = [ReviewUserOrReadOnly]
    # serializer_class = WatchlistSerializer
    # queryset = Watchlist.objects.all()
    # serializer_class = WatchlistSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['title','platform__name']
    # search searchs for similarity, filter search for exact same
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['title', 'platform__name']
    # pagination_class = WatchListPagination
    



###############USING MIXINS###########
# class ReviewDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)


# class ReviewList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)




# class StreamPlatformsList(APIView):
#     permission_classes = [AdminOrReadOnly]
#     def get(self, request):
#         platform = StreamPlatforms.objects.all()
#         serializer = StreamPlatformsSerializer(platform, many=True, context={'request': request})
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = StreamPlatformsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=400)


# class StreamPlatformsDetail(APIView):
#     permission_classes = [AdminOrReadOnly]
#     def get(self, request, pk):
#         try:
#             movie = StreamPlatforms.objects.get(pk=pk)
#         except StreamPlatforms.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         serializer = StreamPlatformsSerializer(movie, context={'request': request})
#         return Response(serializer.data)


#     def post(self, request):
#         serializer = StreamPlatformsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=400)

#     def put(self, request, pk):
#         movie = StreamPlatforms.objects.get(pk=pk)
#         serializer = StreamPlatformsSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=400)
        
#     def delete(self, request, pk):
#         movie = StreamPlatforms.objects.get(pk=pk)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



# class WatchListView(APIView):
#     permission_classes = [AdminOrReadOnly]

#     def get(self, request):
#         watchlist = Watchlist.objects.all()
#         serializer = WatchlistSerializer(watchlist, many=True)
#         return Response(serializer.data)
       
    
#     def post(self, request):
#         serializer = WatchlistSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=400)
        

# class WatchDetail(APIView):
#     #to give edit persmission to admin only, user has only read 
#     permission_classes = [AdminOrReadOnly]

#     def get(self, request, pk):
#         try:
#             movie = Watchlist.objects.get(pk=pk)
#         except Watchlist.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         serializer = WatchlistSerializer(movie)
#         return Response(serializer.data)
    
#     def put(self, request, pk):
#         movie = Watchlist.objects.get(pk=pk)
#         serializer = WatchlistSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=400)
        
#     def delete(self, request, pk):
#         movie = Watchlist.objects.get(pk=pk)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class UserDataView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):

        # pk = self.kwargs.get('pk')
        # print(pk)
        # watch = User.objects.get(pk=pk)
        review_user = self.request.user
        print(review_user)
        platform = User.objects.filter(status = True, user=review_user)

        serializer = UserSerializer(
            platform, many=True, context={'request': request})
        return Response(serializer.data)
             

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            review_user = self.request.user
            review_query = User.objects.filter(user=review_user)
            if review_query.exists():
                raise ValidationError("You have already reviewed")
            serializer.save(user=review_user) 

            email = EmailMessage(
            "Gewog Management System",
            "Hello " + serializer.data['Name'] + " you have successfully added Your Data in our system. Please wait for 12 hours, we have to process your details. THANK YOU",
            settings.EMAIL_HOST_USER,
            [serializer.data['email']],
            )
            email.fail_silently = False
            email.send()
    
            
            print(serializer.data)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class MarriageView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        review_user = self.request.user
        platform = Marriage.objects.filter(status = True)

        serializer = MarriageSerializer(
            platform, many=True, context={'request': request})
        return Response(serializer.data)
             

    def post(self, request):
        serializer = MarriageSerializer(data=request.data)
        review_user = self.request.user
        print(review_user)
        if serializer.is_valid():
            review_user = self.request.user
            print(review_user)
            review_query = Marriage.objects.filter(YOUR_CId=review_user)
            if review_query.exists():
                raise ValidationError("You have already reviewed")
            serializer.save() 

            # email = EmailMessage(
            # "Gewog Management System",
            # "Hello " + serializer.data['Name'] + " you have successfully added Your Data in our system. Please wait for 12 hours, we have to process your details. THANK YOU",
            # settings.EMAIL_HOST_USER,
            # [serializer.data['email']],
            # )
            # email.fail_silently = False
            # email.send()
            # print(serializer.data)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)



#################### child 
class ChildView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        review_user = self.request.user
        platform = ChildData.objects.filter(status = True)

        serializer = ChildDataSerializer(
            platform, many=True, context={'request': request})
        return Response(serializer.data)
             

    def post(self, request):
        serializer = ChildDataSerializer(data=request.data)
        review_user = self.request.user
        print(review_user)
        if serializer.is_valid():
            review_user = self.request.user
            print(review_user)
            review_query = ChildData.objects.filter(YOUR_CId=review_user)
            if review_query.exists():
                raise ValidationError("You have already reviewed")
            serializer.save() 

            # email = EmailMessage(
            # "Gewog Management System",
            # "Hello " + serializer.data['Name'] + " you have successfully added Your Data in our system. Please wait for 12 hours, we have to process your details. THANK YOU",
            # settings.EMAIL_HOST_USER,
            # [serializer.data['email']],
            # )
            # email.fail_silently = False
            # email.send()
            # print(serializer.data)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)




# @api_view(['GET', 'POST'])  
# def movie_list(request):
#     if request.method == 'GET':
#         movie = Watchlist.objects.all()
#         serializer = Watchlisterializer(movie, many=True)
#         return Response(serializer.data)
#     if request.method == 'POST':
#         serializer = Watchlisterializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=400)
             
# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_details(request, pk):
#     if request.method == 'GET':
#         movie = Watchlist.objects.get(pk=pk)
#         serializer = Watchlisterializer(movie)
#         return Response(serializer.data)
#     if request.method == 'PUT': # requests_oauthlib                 
#         serializer = Watchlisterializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=400)
#     if request.method == 'DELETE':
#         movie = Watchlist.objects.get(pk=pk)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class MaleUserDataView(APIView):
#     permission_classes = [IsAuthenticated]
#     def get(self, request):
#         platform = User.objects.filter(status = True)
#         serializer = UserSerializer(
#             platform, many=True, context={'request': request})
#         return Response(serializer.data)
        

#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save() 

            # email = EmailMessage(
            # "Gewog Management System",
            # "Hello " + serializer.data['Name'] + " you have successfully added Your Data in our system. Please wait for 12 hours, we have to process your details. THANK YOU",
            # settings.EMAIL_HOST_USER,
            # [serializer.data['email']],
            # )
            # email.fail_silently = False
            # email.send()
    
            
            # print(serializer.data)
        #     return Response(serializer.data)
        # else:
        #     return Response(serializer.errors)

    # def perform_create(self, serializer):
    #    pk = self.kwargs.get('pk')
    #    watch = Watchlist.objects.get(pk=pk)

    #    review_user = self.request.user
       
    #    review_query = Review.objects.filter(Watchlist = watch, review_user=review_user)

    #    if review_query.exists():
    #     raise ValidationError("You have already reviewed")
    
    #    if watch.no_of_rating == 0:
    #     watch.avg_rating = serializer.validated_data['rating']
    #    else:
    #     watch.avg_rating = (watch.avg_rating + serializer.validated_data['rating'])/2
       
    #    watch.no_of_rating = watch.no_of_rating + 1
    #    watch.save()

    #    serializer.save(Watchlist = watch, review_user = review_user)



    