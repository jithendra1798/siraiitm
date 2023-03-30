from django.contrib import admin
from accounts.models import CustomUser
# from django.contrib.auth.forms import UserChangeForm, UserCreationForm
# import phonenumber_field
from django.contrib.auth.admin import UserAdmin

# Overriding Inbuilt forms.UsernameField with formfields.PhoneNumberField
# class UsernameField(phonenumber_field.formfields.PhoneNumberField):
#     # def to_python(self, value):
#     #     return unicodedata.normalize("NFKC", super().to_python(value))

#     def widget_attrs(self, widget):
#         return {
#             **super().widget_attrs(widget),
#             "autocapitalize": "none",
#             "autocomplete": "username",
#         }

# UserChangeForm.Meta.field_classes['username'] = UsernameField
# UserCreationForm.Meta.field_classes['username'] = UsernameField

# UserAdmin.form = UserChangeForm
# UserAdmin.add_form = UserCreationForm

class CustomUserAdmin(UserAdmin):
    # form = UserChangeForm
    # form.Meta.field_classes['username'] = UsernameField
    # add_form = UserCreationForm
    # add_form.Meta.field_classes['username'] = UsernameField
    list_display = (
        'username', 'first_name', 'gender','is_on_break',
        'is_staff', 'image_tag', 'last_updated'
        )
    list_filter = ("is_staff", "is_superuser", "is_active", "groups")
    search_fields = ("username", "first_name", "last_name", "email")
    ordering = ("username", "-is_staff", )
    readonly_fields = (
        'date_joined', 'last_login', 'last_updated', 'id', 'image_tag'
    )

    fieldsets = (
        (None, {
            'fields': ( 'username', 'password', )
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email', 'mobile',
                       'date_of_birth', 'gender', 'photo', 'image_tag')
        }),
        ('Permissions', {
            'classes': ('wide',),
            'fields': (
                'is_on_break', 'is_phone_verified', 'is_active', 'is_staff',
                'is_superuser', 'groups', 'user_permissions'
                )
        }),
        ('Important dates', {
            # 'classes': ('collapse',),
            'fields': ('last_login', 'date_joined', 'last_updated')
        }),
        ('Additional Info', {
            # 'classes': ('collapse',),
            'fields': ('id', )
        })
    )
    # Fields displayed on Add object page
    add_fieldsets = (
        (None, {
            'fields': ('username', 'password1', 'password2')
        }),
        # ('Personal info', {
        #     'fields': ('first_name', 'last_name', 'email')
        # }),
        # ('Permissions', {
        #     'fields': (
        #         'is_active', 'is_staff', 'is_superuser',
        #         'groups', 'user_permissions'
        #         )
        # }),
        # ('Important dates', {
        #     'fields': ('date_of_birth', 'last_login', 'date_joined')
        # }),
        # ('Additional info', {
        #     'fields': ('photo', 'gender', 'is_genuine')
        # })
    )
admin.site.register(CustomUser, CustomUserAdmin)
