from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Team, Member

# Customize how CustomUser is displayed in admin
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'role', 'is_staff', 'is_active']
    fieldsets = UserAdmin.fieldsets + (
        ('Role Info', {'fields': ('role',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Team)
admin.site.register(Member)
