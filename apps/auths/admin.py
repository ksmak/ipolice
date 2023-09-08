from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model


class MyUserAdmin(UserAdmin):
    list_display = (
        'username',
        'name',
        'surname',
        'patronymic',
        'is_active',
        'is_staff',
        'is_superuser',
        'date_of_creation',
        'date_of_change'
    )

    list_filter = (
        'username',
        'name',
        'surname',
        'patronymic',
    )

    fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': (
                'username',
                'password',
            )
        }),
        ('Ф.И.О.', {
            'classes': ('wide', ),
            'fields': (
                'name',
                'surname',
                'patronymic',
            )
        }),
        ('Разрешения', {
            'classes': ('wide', ),
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
            )
        })
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': (
                'username',
                'password1',
                'password2',
            )
        }),
        ('Ф.И.О.', {
            'classes': ('wide', ),
            'fields': (
                'name',
                'surname',
                'patronymic',
            )
        }),
        ('Разрешения', {
            'classes': ('wide', ),
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
            )
        })
    )

    search_fields = ('username', )

    ordering = ('username', )

    readonly_fields = ('is_superuser', )


admin.site.register(get_user_model(), MyUserAdmin)
