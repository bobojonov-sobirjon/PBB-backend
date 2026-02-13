from rest_framework import serializers
from .models import MainCategory, SubCategory, ServiceDetails, Category, OurProject, WorkStep, YouTubeVideo, WhyChooseUs, ClientReview, CallbackRequest


class ServiceDetailsSerializer(serializers.ModelSerializer):
    """Serializer для деталей услуг"""
    
    class Meta:
        model = ServiceDetails
        fields = ['id', 'image', 'order', 'created_at']


class SubCategorySerializer(serializers.ModelSerializer):
    """Serializer для подкатегорий"""
    service_details = ServiceDetailsSerializer(many=True, read_only=True)
    
    class Meta:
        model = SubCategory
        fields = ['id', 'name', 'is_active', 'created_at', 'service_details']


class MainCategoryWithSubsSerializer(serializers.ModelSerializer):
    """Serializer для главных категорий с подкатегориями"""
    sub_category_list = serializers.SerializerMethodField()
    
    class Meta:
        model = MainCategory
        fields = ['id', 'name', 'is_active', 'created_at', 'sub_category_list']
    
    def get_sub_category_list(self, obj):
        """Получаем список подкатегорий для главной категории"""
        subcategories = SubCategory.objects.filter(parent=obj, is_active=True)
        return SubCategorySerializer(subcategories, many=True, context=self.context).data


class OurProjectSerializer(serializers.ModelSerializer):
    """Serializer для наших проектов"""
    
    class Meta:
        model = OurProject
        fields = ['id', 'image', 'created_at']


class WorkStepSerializer(serializers.ModelSerializer):
    """Serializer для шагов работы"""
    
    class Meta:
        model = WorkStep
        fields = ['id', 'step_number', 'title', 'description', 'image', 'created_at']


class YouTubeVideoSerializer(serializers.ModelSerializer):
    """Serializer для YouTube видео"""
    
    class Meta:
        model = YouTubeVideo
        fields = ['id', 'title', 'youtube_url', 'thumbnail', 'viewers', 'created_at']


class WhyChooseUsSerializer(serializers.ModelSerializer):
    """Serializer для преимуществ"""
    
    class Meta:
        model = WhyChooseUs
        fields = ['id', 'title', 'description', 'order', 'created_at']


class ClientReviewSerializer(serializers.ModelSerializer):
    """Serializer для отзывов клиентов"""
    
    class Meta:
        model = ClientReview
        fields = ['id', 'full_name', 'comment', 'rating', 'created_at']
        read_only_fields = ['id', 'created_at']


class ClientReviewCreateSerializer(serializers.ModelSerializer):
    """Serializer для создания отзывов"""
    
    class Meta:
        model = ClientReview
        fields = ['full_name', 'comment', 'rating']
    
    def validate_rating(self, value):
        """Валидация рейтинга"""
        if value < 1 or value > 5:
            raise serializers.ValidationError("Рейтинг должен быть от 1 до 5")
        return value


class CallbackRequestSerializer(serializers.ModelSerializer):
    """Serializer для заявок на обратный звонок"""
    
    class Meta:
        model = CallbackRequest
        fields = ['id', 'name', 'phone', 'created_at']
        read_only_fields = ['id', 'created_at']
    
    def validate_phone(self, value):
        """Валидация телефона"""
        # Удаляем все нечисловые символы
        phone_digits = ''.join(filter(str.isdigit, value))
        if len(phone_digits) < 10:
            raise serializers.ValidationError("Некорректный номер телефона")
        return value
