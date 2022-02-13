from django.contrib import admin
from .models import Genre
from .models import Kinds
from .models import Clothes

admin.site.register(Genre)
admin.site.register(Kinds)
admin.site.register(Clothes)