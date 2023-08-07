from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Profile
from .forms import ProfileForm
from django.utils.safestring import mark_safe
from django.db.models import ImageField


# Register your models here.

admin.site.register(add_links)
admin.site.register(menu_bd)
admin.site.register(phone)


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

    def thumbnail(self, obj):
        return obj.avatar.url if obj.avatar else None

    thumbnail.short_description = 'Avatar'

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)
    form = ProfileForm

    # def save_model(self, request, obj, form, change):
    #     """Сохранить расширенную модель профиля"""
    #     if obj.pk is None:
    #         obj.save()
    #         profile = Profile(user=obj)
    #         profile.save()
    #     else:
    #         obj.save()

    # def get_thumbnail_html(self, obj):
    #     thumbnail_url = obj.profile.avatar.url if obj.profile.avatar else None
    #     if thumbnail_url:
    #         return mark_safe(f"<img src='{thumbnail_url}' width: 50px>")
    #     return ''

    # def get_queryset(self, request):
    #     return super().get_queryset(request).prefetch_related('profile')
    #
    # get_thumbnail_html.short_description = 'Thumbnail'
    # get_thumbnail_html.allow_tags = True

    list_display = ['username','email', 'first_name', 'last_name']

    ordering = ['first_name', 'last_name', 'username']

#admin.site.unregister(User)
admin.site.register(Profile)
#admin.site.register(User, UserAdmin)