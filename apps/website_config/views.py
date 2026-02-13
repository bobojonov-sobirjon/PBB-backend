from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema, OpenApiParameter
from .models import MainCategory, SubCategory, ServiceDetails, OurProject, WorkStep, YouTubeVideo, WhyChooseUs, ClientReview, CallbackRequest
from .serializers import (
    MainCategoryWithSubsSerializer, ServiceDetailsSerializer, OurProjectSerializer, 
    WorkStepSerializer, YouTubeVideoSerializer, WhyChooseUsSerializer, 
    ClientReviewSerializer, ClientReviewCreateSerializer, CallbackRequestSerializer
)


class MainCategoryListView(generics.ListAPIView):
    """
    API для получения списка главных категорий с подкатегориями
    """
    queryset = MainCategory.objects.filter(is_active=True)
    serializer_class = MainCategoryWithSubsSerializer
    
    @extend_schema(
        summary="Список главных категорий",
        description="Получить список всех главных категорий с их подкатегориями",
        tags=["Категории"]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class SubCategoryServiceDetailsView(APIView):
    """
    API для получения деталей услуг по ID подкатегории
    """
    
    @extend_schema(
        summary="Детали услуг подкатегории",
        description="Получить список деталей услуг для конкретной подкатегории",
        parameters=[
            OpenApiParameter(
                name='sub_category_id',
                type=int,
                location=OpenApiParameter.QUERY,
                description='ID подкатегории',
                required=True
            )
        ],
        tags=["Категории"]
    )
    def get(self, request):
        """Получить детали услуг по ID подкатегории"""
        sub_category_id = request.query_params.get('sub_category_id')
        
        if not sub_category_id:
            return Response(
                {"error": "Параметр sub_category_id обязателен"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            sub_category = SubCategory.objects.get(id=sub_category_id, is_active=True)
        except SubCategory.DoesNotExist:
            return Response(
                {"error": "Подкатегория не найдена"},
                status=status.HTTP_404_NOT_FOUND
            )
        
        service_details = ServiceDetails.objects.filter(category=sub_category)
        serializer = ServiceDetailsSerializer(service_details, many=True, context={'request': request})
        
        return Response({
            "sub_category_id": sub_category.id,
            "sub_category_name": sub_category.name,
            "service_details": serializer.data
        })


class OurProjectListView(generics.ListAPIView):
    """
    API для получения списка наших проектов
    """
    queryset = OurProject.objects.all()
    serializer_class = OurProjectSerializer
    pagination_class = None  # Отключаем пагинацию для простого списка
    
    @extend_schema(
        summary="Список наших проектов",
        description="Получить список всех фотографий проектов",
        tags=["Проекты"]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class WorkStepListView(generics.ListAPIView):
    """
    API для получения списка шагов работы
    """
    queryset = WorkStep.objects.all()
    serializer_class = WorkStepSerializer
    pagination_class = None  # Отключаем пагинацию для простого списка
    
    @extend_schema(
        summary="Список шагов работы",
        description="Получить список всех шагов работы (5 шагов)",
        tags=["Шаги работы"]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class YouTubeVideoListView(generics.ListAPIView):
    """
    API для получения списка YouTube видео
    """
    queryset = YouTubeVideo.objects.all()
    serializer_class = YouTubeVideoSerializer
    pagination_class = None  # Отключаем пагинацию для простого списка
    
    @extend_schema(
        summary="Список YouTube видео",
        description="Получить список всех YouTube видео",
        tags=["YouTube Видео"]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class IncrementVideoViewsView(APIView):
    """
    API для увеличения счетчика просмотров видео
    """
    
    @extend_schema(
        summary="Увеличить просмотры видео",
        description="Увеличить счетчик просмотров для конкретного YouTube видео на +1",
        parameters=[
            OpenApiParameter(
                name='id',
                type=int,
                location=OpenApiParameter.QUERY,
                description='ID видео',
                required=True
            )
        ],
        tags=["YouTube Видео"]
    )
    def post(self, request):
        """Увеличить счетчик просмотров видео"""
        video_id = request.query_params.get('id')
        
        if not video_id:
            return Response(
                {"error": "Параметр id обязателен"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            video = YouTubeVideo.objects.get(id=video_id)
            video.viewers += 1
            video.save()
            
            serializer = YouTubeVideoSerializer(video, context={'request': request})
            return Response({
                "success": True,
                "message": "Просмотры увеличены",
                "video": serializer.data
            })
        except YouTubeVideo.DoesNotExist:
            return Response(
                {"error": "Видео не найдено"},
                status=status.HTTP_404_NOT_FOUND
            )


class WhyChooseUsListView(generics.ListAPIView):
    """
    API для получения списка преимуществ
    """
    queryset = WhyChooseUs.objects.filter(is_active=True)
    serializer_class = WhyChooseUsSerializer
    pagination_class = None  # Отключаем пагинацию для простого списка
    
    @extend_schema(
        summary="Почему выбирают нас",
        description="Получить список всех преимуществ компании",
        tags=["Преимущества"]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class ClientReviewListView(generics.ListAPIView):
    """
    API для получения списка отзывов клиентов
    """
    queryset = ClientReview.objects.filter(is_active=True)
    serializer_class = ClientReviewSerializer
    pagination_class = None  # Отключаем пагинацию для простого списка
    
    @extend_schema(
        summary="Отзывы клиентов",
        description="Получить список всех отзывов клиентов",
        tags=["Отзывы"]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class ClientReviewCreateView(generics.CreateAPIView):
    """
    API для создания отзыва клиента
    """
    serializer_class = ClientReviewCreateSerializer
    
    @extend_schema(
        summary="Оставить отзыв",
        description="Создать новый отзыв клиента",
        tags=["Отзывы"],
        request=ClientReviewCreateSerializer,
        responses={201: ClientReviewSerializer}
    )
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            review = serializer.save(is_active=False)  # По умолчанию неактивен (модерация)
            return Response(
                {
                    "success": True,
                    "message": "Отзыв успешно отправлен и будет опубликован после модерации",
                    "review": ClientReviewSerializer(review).data
                },
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CallbackRequestCreateView(generics.CreateAPIView):
    """
    API для создания заявки на обратный звонок
    """
    serializer_class = CallbackRequestSerializer
    
    @extend_schema(
        summary="Заказать обратный звонок",
        description="Создать заявку на обратный звонок",
        tags=["Заявки"],
        request=CallbackRequestSerializer,
        responses={201: CallbackRequestSerializer}
    )
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            callback = serializer.save()
            return Response(
                {
                    "success": True,
                    "message": "Заявка успешно отправлена! Мы свяжемся с вами в ближайшее время",
                    "callback": CallbackRequestSerializer(callback).data
                },
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
