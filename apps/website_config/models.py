from django.db import models


class Category(models.Model):
    """Базовая модель категории"""
    name = models.CharField(max_length=255, verbose_name="Название")
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children', verbose_name="Родительская категория")
    is_active = models.BooleanField(default=True, verbose_name="Активна")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        db_table = 'categories'
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['name']

    def __str__(self):
        return self.name


class MainCategoryManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(parent__isnull=True)


class MainCategory(Category):
    """Прокси модель для главных категорий"""
    objects = MainCategoryManager()

    class Meta:
        proxy = True
        verbose_name = "Главная категория"
        verbose_name_plural = "01. Главные категории"


class SubCategoryManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(parent__isnull=False)


class SubCategory(Category):
    """Прокси модель для подкатегорий"""
    objects = SubCategoryManager()

    class Meta:
        proxy = True
        verbose_name = "Подкатегория"
        verbose_name_plural = "02. Подкатегории"


class ServiceDetails(models.Model):
    """Детали услуг для подкатегорий"""
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='service_details', verbose_name="Категория")
    image = models.ImageField(upload_to='services/details/', verbose_name="Изображение")
    order = models.IntegerField(default=0, verbose_name="Порядок")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        db_table = 'service_details'
        verbose_name = "Деталь услуги"
        verbose_name_plural = "Детали услуг"
        ordering = ['order', 'created_at']

    def __str__(self):
        return f"Деталь для {self.category.name}"


class OurProject(models.Model):
    """Наши проекты - галерея проектов"""
    image = models.ImageField(upload_to='projects/', verbose_name="Изображение")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        db_table = 'our_projects'
        verbose_name = "Наш проект"
        verbose_name_plural = "03. Наши проекты"
        ordering = ['-created_at']

    def __str__(self):
        return f"Проект #{self.id}"


class WorkStep(models.Model):
    """Шаги работы (Для старта всего 5 шагов)"""
    step_number = models.IntegerField(unique=True, verbose_name="Номер шага")
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to='work_steps/', verbose_name="Изображение")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        db_table = 'work_steps'
        verbose_name = "Шаг работы"
        verbose_name_plural = "04. Шаги работы"
        ordering = ['step_number']

    def __str__(self):
        return f"Шаг {self.step_number}: {self.title}"


class YouTubeVideo(models.Model):
    """YouTube видео"""
    title = models.CharField(max_length=255, verbose_name="Название")
    youtube_url = models.URLField(verbose_name="Ссылка YouTube")
    thumbnail = models.ImageField(upload_to='youtube_thumbnails/', blank=True, null=True, verbose_name="Обложка")
    viewers = models.IntegerField(default=0, verbose_name="Просмотров")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        db_table = 'youtube_videos'
        verbose_name = "YouTube видео"
        verbose_name_plural = "05. YouTube видео"
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class WhyChooseUs(models.Model):
    """Почему выбирают нас (Преимущества)"""
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    order = models.IntegerField(default=0, verbose_name="Порядок")
    is_active = models.BooleanField(default=True, verbose_name="Активно")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        db_table = 'why_choose_us'
        verbose_name = "Преимущество"
        verbose_name_plural = "06. Почему выбирают нас"
        ordering = ['order', 'created_at']

    def __str__(self):
        return self.title


class ClientReview(models.Model):
    """Отзывы клиентов"""
    full_name = models.CharField(max_length=255, verbose_name="ФИО клиента")
    comment = models.TextField(verbose_name="Отзыв")
    rating = models.IntegerField(default=5, verbose_name="Рейтинг", 
                                 help_text="От 1 до 5 звезд")
    is_active = models.BooleanField(default=True, verbose_name="Активно")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        db_table = 'client_reviews'
        verbose_name = "Отзыв клиента"
        verbose_name_plural = "07. Отзывы клиентов"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.full_name} - {self.rating}★"


class CallbackRequest(models.Model):
    """Заявки на обратный звонок"""
    name = models.CharField(max_length=255, verbose_name="Имя")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    is_processed = models.BooleanField(default=False, verbose_name="Обработано")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        db_table = 'callback_requests'
        verbose_name = "Заявка на звонок"
        verbose_name_plural = "08. Заявки на обратный звонок"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.phone}"
