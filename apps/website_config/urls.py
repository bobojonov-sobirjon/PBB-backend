from django.urls import path
from .views import (
    MainCategoryListView, 
    SubCategoryServiceDetailsView, 
    OurProjectListView, 
    WorkStepListView, 
    YouTubeVideoListView,
    IncrementVideoViewsView,
    WhyChooseUsListView,
    ClientReviewListView,
    ClientReviewCreateView,
    CallbackRequestCreateView
)


urlpatterns = [
    path('categories/', MainCategoryListView.as_view(), name='main-categories-list'),
    path('service-details/', SubCategoryServiceDetailsView.as_view(), name='service-details'),
    path('projects/', OurProjectListView.as_view(), name='our-projects-list'),
    path('work-steps/', WorkStepListView.as_view(), name='work-steps-list'),
    path('youtube-videos/', YouTubeVideoListView.as_view(), name='youtube-videos-list'),
    path('youtube-videos/increment-views/', IncrementVideoViewsView.as_view(), name='increment-video-views'),
    path('why-choose-us/', WhyChooseUsListView.as_view(), name='why-choose-us-list'),
    path('client-reviews/', ClientReviewListView.as_view(), name='client-reviews-list'),
    path('client-reviews/create/', ClientReviewCreateView.as_view(), name='client-review-create'),
    path('callback-request/', CallbackRequestCreateView.as_view(), name='callback-request-create'),
]