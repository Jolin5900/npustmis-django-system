import os
from pathlib import Path
from dotenv import load_dotenv
import dj_database_url  # 新增：支援 PostgreSQL

load_dotenv()  # 保留你原本的 .env 讀取

BASE_DIR = Path(__file__).resolve().parent.parent

# === 安全設定 ===
SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-your-secret-key')  # Render 會自動覆蓋
DEBUG = False  # 上線必須 False
ALLOWED_HOSTS = [os.environ.get('RENDER_EXTERNAL_HOSTNAME', 'https://npustmis-django-system.onrender.com/')]
#ALLOWED_HOSTS = ['*']  # Render 支援所有域名

# === 應用程式 ===
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
]

# === Middleware（加入 WhiteNoise）===
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # 新增：靜態檔案
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'system.urls'
LOGIN_REDIRECT_URL = '/dashboard/'
LOGOUT_REDIRECT_URL = '/logout/'

# === 模板 ===
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'system.wsgi.application'

# === 資料庫：本地用 SQLite，Render 用 PostgreSQL ===
DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///' + str(BASE_DIR / 'db.sqlite3')
    )
}

# === 靜態與媒體檔案 ===
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'  # Render 收集靜態檔案的位置
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'  # 壓縮 + 快取

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'