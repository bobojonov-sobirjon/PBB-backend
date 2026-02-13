from django.core.management.base import BaseCommand
from apps.website_config.models import (
    MainCategory, SubCategory, ServiceDetails, 
    OurProject, WorkStep, YouTubeVideo, WhyChooseUs, ClientReview
)


class Command(BaseCommand):
    help = 'Создать тестовые данные для всех моделей'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Начинаем создание тестовых данных...'))

        # Очистка существующих данных
        self.stdout.write('Очистка существующих данных...')
        ClientReview.objects.all().delete()
        WhyChooseUs.objects.all().delete()
        YouTubeVideo.objects.all().delete()
        WorkStep.objects.all().delete()
        OurProject.objects.all().delete()
        ServiceDetails.objects.all().delete()
        SubCategory.objects.all().delete()
        MainCategory.objects.all().delete()

        # Создание главных категорий
        self.stdout.write('Создание главных категорий...')
        ekonom = MainCategory.objects.create(
            name='Эконом ремонт',
            is_active=True
        )
        
        standart = MainCategory.objects.create(
            name='Стандартный ремонт',
            is_active=True
        )
        
        dizain = MainCategory.objects.create(
            name='Дизайнерский ремонт',
            is_active=True
        )
        
        landshaft = MainCategory.objects.create(
            name='Ландшафтное освещение',
            is_active=True
        )

        # Создание подкатегорий для Эконом ремонт
        self.stdout.write('Создание подкатегорий для Эконом ремонт...')
        SubCategory.objects.create(
            name='Поклейка обоев',
            parent=ekonom,
            is_active=True
        )
        
        SubCategory.objects.create(
            name='Натяжные потолки',
            parent=ekonom,
            is_active=True
        )
        
        SubCategory.objects.create(
            name='Точечное освещение',
            parent=ekonom,
            is_active=True
        )
        
        SubCategory.objects.create(
            name='Укладка ламината',
            parent=ekonom,
            is_active=True
        )
        
        SubCategory.objects.create(
            name='Установка дверей',
            parent=ekonom,
            is_active=True
        )

        # Создание подкатегорий для Стандартный ремонт
        self.stdout.write('Создание подкатегорий для Стандартный ремонт...')
        SubCategory.objects.create(
            name='Подготовительные работы',
            parent=standart,
            is_active=True
        )
        
        SubCategory.objects.create(
            name='Электромонтажные',
            parent=standart,
            is_active=True
        )
        
        SubCategory.objects.create(
            name='Сантехнические, Отделочные',
            parent=standart,
            is_active=True
        )

        # Создание подкатегорий для Дизайнерский ремонт
        self.stdout.write('Создание подкатегорий для Дизайнерский ремонт...')
        SubCategory.objects.create(
            name='Планировочное решение',
            parent=dizain,
            is_active=True
        )
        
        SubCategory.objects.create(
            name='Концепция интерьера',
            parent=dizain,
            is_active=True
        )
        
        SubCategory.objects.create(
            name='3D-визуализация',
            parent=dizain,
            is_active=True
        )
        
        SubCategory.objects.create(
            name='Рабочая документация',
            parent=dizain,
            is_active=True
        )

        # Создание подкатегорий для Ландшафтное освещение
        self.stdout.write('Создание подкатегорий для Ландшафтное освещение...')
        SubCategory.objects.create(
            name='Подсветка',
            parent=landshaft,
            is_active=True
        )
        
        SubCategory.objects.create(
            name='Охранное',
            parent=landshaft,
            is_active=True
        )
        
        SubCategory.objects.create(
            name='Архивное',
            parent=landshaft,
            is_active=True
        )
        
        SubCategory.objects.create(
            name='Маркировочное',
            parent=landshaft,
            is_active=True
        )

        # Создание шагов работы
        self.stdout.write('Создание шагов работы...')
        WorkStep.objects.create(
            step_number=1,
            title='Вы направляете техническое задание',
            description='любым удобным способом электронная почта, мессенджеры'
        )
        
        WorkStep.objects.create(
            step_number=2,
            title='Мы ознакомимся с планом',
            description='и приезжаем на объект для проведения контрольных замеров и подготовки сметы'
        )
        
        WorkStep.objects.create(
            step_number=3,
            title='Совместно обсуждаем проект и прочие вопросы',
            description='в любом удобном формате (он/офлайн)'
        )
        
        WorkStep.objects.create(
            step_number=4,
            title='Согласовываем сметы, подписываем договор',
            description='и выходим на объект'
        )
        
        WorkStep.objects.create(
            step_number=5,
            title='Выполняем работы на объекте',
            description='взаимодействуя с вами, технадзором, субподрядчиками, надзорными службами'
        )

        # Создание YouTube видео
        self.stdout.write('Создание YouTube видео...')
        YouTubeVideo.objects.create(
            title='Ремонт трехкомнатной квартиры',
            youtube_url='https://www.youtube.com/watch?v=dQw4w9WgXcQ',
            viewers=356
        )
        
        YouTubeVideo.objects.create(
            title='Ремонт трехкомнатной квартиры',
            youtube_url='https://www.youtube.com/watch?v=dQw4w9WgXcQ',
            viewers=356
        )
        
        YouTubeVideo.objects.create(
            title='Ремонт трехкомнатной квартиры',
            youtube_url='https://www.youtube.com/watch?v=dQw4w9WgXcQ',
            viewers=356
        )
        
        YouTubeVideo.objects.create(
            title='Ремонт трехкомнатной квартиры',
            youtube_url='https://www.youtube.com/watch?v=dQw4w9WgXcQ',
            viewers=356
        )

        # Создание преимуществ (Почему выбирают нас)
        self.stdout.write('Создание преимуществ...')
        WhyChooseUs.objects.create(
            title='ДОСТУПНОСТЬ',
            description='6 дневная рабочая неделя (с понедельника по субботу), рабочий день длится 8 часов.',
            order=1,
            is_active=True
        )
        
        WhyChooseUs.objects.create(
            title='ПРОФЕССИОНАЛИЗМ',
            description='Вопросы задаем только по делу. Не оставляем лишние дополнительных работ. Выполняем функцию техзаказчика',
            order=2,
            is_active=True
        )
        
        WhyChooseUs.objects.create(
            title='УДОБСТВО',
            description='Работаем с дизайнерскими материалами. Любая форма оплаты. Предоставляем закрывающие документы. Приедем для замеров на объект.',
            order=3,
            is_active=True
        )
        
        WhyChooseUs.objects.create(
            title='ГАРАНТИИ',
            description='Гарантийный срок по ГК РФ. Сервисное обслуживание. Страхование на период СМР. Финансовая ответственность',
            order=4,
            is_active=True
        )
        
        WhyChooseUs.objects.create(
            title='ВНИМАТЕЛЬНОСТЬ',
            description='К пожеланиям заказчика. На совещаниях о проектных правках. Обращаем внимание на детали и мелочи. Всегда убираем за собой мусор.',
            order=5,
            is_active=True
        )
        
        WhyChooseUs.objects.create(
            title='ОТВЕТСТВЕННОСТЬ',
            description='Перед взятыми на себя обязательствами. За соблюдение сроков. Поддерживаем культуру производства работ. Контролируем качество выполнения работ.',
            order=6,
            is_active=True
        )

        # Создание отзывов клиентов
        self.stdout.write('Создание отзывов клиентов...')
        ClientReview.objects.create(
            full_name='Иванов Сергей Владимирович',
            comment='Хочу поблагодарить компанию ПВВ Строй! Я доволен все мои направлений нет. Мой проект закончили даже раньше срока.',
            rating=5,
            is_active=True
        )
        
        ClientReview.objects.create(
            full_name='Николай Власович',
            comment='Все понравилось, спасибо, сделали работу быстро и качественно рекомендую!',
            rating=5,
            is_active=True
        )
        
        ClientReview.objects.create(
            full_name='Стрелков Евгений Юрьевич',
            comment='Спасибо большое за работу! Установили фундамент быстро, качественно провели монтаж. Работа сделана оперативно, ребята приятные, отзывчивые!',
            rating=5,
            is_active=True
        )
        
        ClientReview.objects.create(
            full_name='Вадим Алексеев',
            comment='Работа выполнена на высоком уровне, аккуратно и качественно, все сделали очень быстро. обращайтесь только к ним!',
            rating=5,
            is_active=True
        )

        self.stdout.write(self.style.SUCCESS('Тестовые данные успешно созданы!'))
        self.stdout.write(f'  - Главных категорий: {MainCategory.objects.count()}')
        self.stdout.write(f'  - Подкатегорий: {SubCategory.objects.count()}')
        self.stdout.write(f'  - Шагов работы: {WorkStep.objects.count()}')
        self.stdout.write(f'  - YouTube видео: {YouTubeVideo.objects.count()}')
        self.stdout.write(f'  - Преимуществ: {WhyChooseUs.objects.count()}')
        self.stdout.write(f'  - Отзывов клиентов: {ClientReview.objects.count()}')
