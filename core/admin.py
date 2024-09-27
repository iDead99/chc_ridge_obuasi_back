from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Member
from django.contrib import admin

# @admin.register(User)
# class UserAdmin(BaseUserAdmin):
#     list_display = ["first_name", "last_name", "email", "phone", "residence", "gps_address", "is_staff"]
#     ordering = ["email"]
    
#     fieldsets = (
#         (None, {"fields": ("email", "password")}),
#         ("Personal info", {"fields": ("first_name", "last_name")}),
#         ("Permissions", {
#             "fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions"),
#         }),
#         ("Important dates", {"fields": ("last_login", "date_joined")}),
#     )
    
#     add_fieldsets = (
#         (None, {
#             "classes": ("wide",),
#             "fields": ("email", "password1", "password2", "first_name", "last_name"),
#         }),
#     )

#     search_fields = ("email", "first_name", "last_name")
#     ordering = ("email",)
#     filter_horizontal = ("groups", "user_permissions")


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "email", "phone", "residence", "gps_address", "date_registered"]
    ordering = ["first_name", "last_name", "date_registered"]
    exclude = ["date_registered"]