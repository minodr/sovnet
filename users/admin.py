from django.contrib import admin

from users.models import User


class UserAdmin(admin.ModelAdmin):
    class Meta:
        model = User

    list_display = ["id", "username", "email", "password"]
    search_fields = ["username", "email"]
    ordering = ["id", "username"]


admin.site.register(User, UserAdmin)
