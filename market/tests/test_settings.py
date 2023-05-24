import shutil
import tempfile

from django.conf import settings
from django.test import TestCase
from market.models import Product, Category
from django.contrib.auth.models import User


class Settings(TestCase):
    @classmethod
    def setUpClass(cls):
        super(Settings, cls).setUpClass()

        cls.category = Category.objects.create(title='electronics', slug='electronics')
        cls.login = 'stupk'
        cls.login2 = 'rob'
        cls.password = 'qwer123456789'

        cls.owner = User.objects.create_superuser(username=cls.login, email='dod@gmail.com',
                                      password=cls.password)

        cls.unprivileged_user = User.objects.create_user(username=cls.login2, email='fff@gmail.com',
                                                         password=cls.password)
        # Создаем временную папку для медиа-файлов;
        # на момент теста медиа папка будет переопределена
        settings.MEDIA_ROOT = tempfile.mkdtemp(dir=settings.BASE_DIR)
        cls.product = Product.objects.create(name='Car', text='some text',
                                             price=14.52, owner=cls.owner, category=cls.category,
                                             picture=tempfile.NamedTemporaryFile(suffix='.png').name)

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        # рекурсивно удаляем временную папку после завершения тестов
        shutil.rmtree(settings.MEDIA_ROOT, ignore_errors=True)

