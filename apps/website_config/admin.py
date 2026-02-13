from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.utils.html import format_html
from .models import MainCategory, SubCategory, ServiceDetails, Category, OurProject, WorkStep, YouTubeVideo, WhyChooseUs, ClientReview, CallbackRequest


class ServiceDetailsInline(admin.TabularInline):
    """Inline для деталей услуг в подкатегориях"""
    model = ServiceDetails
    extra = 1
    fields = ('image', 'image_preview', 'order')
    readonly_fields = ('image_preview',)
    verbose_name = "Деталь услуги"
    verbose_name_plural = "Детали услуг"

    def image_preview(self, obj):
        """Предварительный просмотр изображения"""
        if obj.image:
            return format_html('<img src="{}" style="max-height: 80px; max-width: 150px;" />', obj.image.url)
        return "Нет изображения"
    
    image_preview.short_description = "Предпросмотр"


@admin.register(MainCategory)
class MainCategoryAdmin(admin.ModelAdmin):
    """Админка для главных категорий"""
    list_display = ('name', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('name',)
    list_editable = ('is_active',)
    fields = ('name', 'is_active')
    readonly_fields = ()

    def get_queryset(self, request):
        """Показываем только главные категории (без родителя)"""
        return super().get_queryset(request).filter(parent__isnull=True)

    def save_model(self, request, obj, form, change):
        """При сохранении главной категории, parent должен быть None"""
        obj.parent = None
        super().save_model(request, obj, form, change)


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    """Админка для подкатегорий"""
    list_display = ('name', 'parent', 'is_active', 'created_at')
    list_filter = ('is_active', 'parent', 'created_at')
    search_fields = ('name',)
    list_editable = ('is_active',)
    fields = ('name', 'parent', 'is_active')
    inlines = [ServiceDetailsInline]

    def get_queryset(self, request):
        """Показываем только подкатегории (с родителем)"""
        return super().get_queryset(request).filter(parent__isnull=False)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        """При выборе родительской категории показываем только главные категории"""
        if db_field.name == "parent":
            kwargs["queryset"] = Category.objects.filter(parent__isnull=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(OurProject)
class OurProjectAdmin(admin.ModelAdmin):
    """Админка для наших проектов"""
    list_display = ('image_preview', 'created_at')
    list_filter = ('created_at',)
    fields = ('image', 'image_preview')
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        """Предварительный просмотр изображения"""
        if obj.image:
            return format_html('<img src="{}" style="max-height: 100px; max-width: 200px;" />', obj.image.url)
        return "Нет изображения"
    
    image_preview.short_description = "Предпросмотр"


@admin.register(WorkStep)
class WorkStepAdmin(admin.ModelAdmin):
    """Админка для шагов работы"""
    list_display = ('image_preview', 'title', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title', 'description')
    fields = ('step_number', 'title', 'description', 'image', 'image_preview')
    readonly_fields = ('image_preview',)
    ordering = ('step_number',)

    def image_preview(self, obj):
        """Предварительный просмотр изображения"""
        if obj.image:
            return format_html('<img src="{}" style="max-height: 100px; max-width: 200px;" />', obj.image.url)
        return "Нет изображения"
    
    image_preview.short_description = "Предпросмотр"


@admin.register(YouTubeVideo)
class YouTubeVideoAdmin(admin.ModelAdmin):
    """Админка для YouTube видео"""
    list_display = ('thumbnail_preview', 'title', 'viewers', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title',)
    fields = ('title', 'youtube_url', 'thumbnail', 'thumbnail_preview', 'viewers')
    readonly_fields = ('thumbnail_preview', 'viewers')

    def thumbnail_preview(self, obj):
        """Предварительный просмотр обложки"""
        if obj.thumbnail:
            return format_html('<img src="{}" style="max-height: 100px; max-width: 200px;" />', obj.thumbnail.url)
        return "Нет обложки"
    
    thumbnail_preview.short_description = "Предпросмотр"


@admin.register(WhyChooseUs)
class WhyChooseUsAdmin(admin.ModelAdmin):
    """Админка для преимуществ"""
    list_display = ('title', 'order', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('title', 'description')
    list_editable = ('order', 'is_active')
    fields = ('title', 'description', 'order', 'is_active')
    ordering = ('order',)


@admin.register(ClientReview)
class ClientReviewAdmin(admin.ModelAdmin):
    """Админка для отзывов клиентов"""
    list_display = ('full_name', 'rating_stars', 'is_active', 'created_at')
    list_filter = ('is_active', 'rating', 'created_at')
    search_fields = ('full_name', 'comment')
    list_editable = ('is_active',)
    fields = ('full_name', 'comment', 'rating', 'is_active')
    readonly_fields = ('rating_stars',)

    def rating_stars(self, obj):
        """Показать рейтинг звездами"""
        stars = '⭐' * obj.rating
        return format_html('<span style="font-size: 18px;">{}</span>', stars)
    
    rating_stars.short_description = "Рейтинг"


@admin.register(CallbackRequest)
class CallbackRequestAdmin(admin.ModelAdmin):
    """Админка для заявок на обратный звонок"""
    list_display = ('name', 'phone', 'is_processed', 'created_at')
    list_filter = ('is_processed', 'created_at')
    search_fields = ('name', 'phone')
    list_editable = ('is_processed',)
    readonly_fields = ('created_at',)
    fields = ('name', 'phone', 'is_processed', 'created_at')


# Unregister default User and Group models
try:
    admin.site.unregister(User)
except admin.sites.NotRegistered:
    pass

try:
    admin.site.unregister(Group)
except admin.sites.NotRegistered:
    pass


# Customize admin site headers
admin.site.site_header = "PBB Администрация"
admin.site.site_title = "PBB Admin"
admin.site.index_title = "Панель управления PBB"
