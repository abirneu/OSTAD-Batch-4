from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Job, Application

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_employer', 'is_applicant', 'is_staff')
    list_filter = ('is_employer', 'is_applicant', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Roles', {'fields': ('is_employer', 'is_applicant')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_employer', 'is_applicant'),
        }),
    )

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company_name', 'location', 'posted_by', 'created_at')
    list_filter = ('location', 'created_at', 'posted_by')
    search_fields = ('title', 'company_name', 'description', 'posted_by__username')
    raw_id_fields = ('posted_by',)
    date_hierarchy = 'created_at'

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('job', 'applicant', 'applied_at', 'status')
    list_filter = ('applied_at', 'status')
    search_fields = ('job__title', 'applicant__username', 'cover_letter')
    raw_id_fields = ('job', 'applicant')
    date_hierarchy = 'applied_at'
    list_editable = ('status',)