from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import Account


class AccountAdmin(UserAdmin):
    list_display = ('username', 'email', 'phone', 'name', 'surname', 'is_staff')
    fieldsets = (
        (_('None'), {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('name', 'surname', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'is_journalist', 'groups', 'user_permissions'),
        }),
        # (_('Important dates'), {'fields': ('date_joined',)}),
        (_('Info'), {'fields': ('phone', 'avatar', 'gender')}),
    )


admin.site.register(Account, AccountAdmin)
