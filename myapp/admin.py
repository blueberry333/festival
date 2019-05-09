from django.contrib import admin

from .models import Board
from .models import Comment
from .models import Comment2
# Register your models here.

admin.site.register(Board)
admin.site.register(Comment)
admin.site.register(Comment2)