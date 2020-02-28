from django.contrib import admin

# Register your models here.
from django.contrib.auth import get_user_model

User = get_user_model()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'username',
        'full_name',
        'email',
        'first_name',
        'last_name',
        'user_type',
        'is_active',
        'is_staff',
        'is_superuser',
        'date_joined',
    ]