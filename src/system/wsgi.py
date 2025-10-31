"""
WSGI config for system project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""
import os
# import sys  <-- 移除
from django.core.wsgi import get_wsgi_application

# 确保这段代码是正确的
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'system.settings')

application = get_wsgi_application()