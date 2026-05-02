from django.contrib import admin
from django.utils.html import format_html
from .models import Application


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):

    list_display = (
        'full_name',
        'email',
        'country',
        'status_badge',
        'python_level',
        'created_at',
    )

    list_filter = (
        'application_status',
        'country',
        'status',
        'python_level',
        'created_at',
        'attend_all',
        'represent_professionally',
    )

    search_fields = (
        'full_name',
        'email',
        'phone',
        'city',
        'field',
    )

    readonly_fields = (
        'created_at',
        'updated_at',
    )

    fieldsets = (
        ('Application Status', {
            'fields': ('application_status', 'created_at', 'updated_at'),
        }),
        ('Personal Information', {
            'fields': (
                'full_name',
                'email',
                'phone',
                'country',
                'city',
                'dob',
                'is_18',
            ),
        }),
        ('Background & Skills', {
            'fields': (
                'status',
                'field',
                'python_level',
                'python_duration',
            ),
        }),
        ('Motivation', {
            'fields': (
                'why_attend',
                'hope_to_gain',
                'interests',
            ),
        }),
        ('Community & Impact', {
            'fields': (
                'community',
                'contributions',
                'knowledge_sharing',
            ),
            'classes': ('collapse',),
        }),
        ('Commitment', {
            'fields': (
                'attend_all',
                'represent_professionally',
                'share_publicly',
                'represent_how',
            ),
        }),
        ('Travel & Documents', {
            'fields': (
                'has_national_id',
                'has_passport',
                'can_travel',
            ),
        }),
        ('Support', {
            'fields': (
                'financial_support',
                'anything_else',
            ),
            'classes': ('collapse',),
        }),
    )

    ordering = ('-created_at',)

    actions = ['mark_as_reviewed', 'mark_as_accepted', 'mark_as_rejected']

    def status_badge(self, obj):
        colors = {
            'submitted': '#FFA500', 
            'reviewed': '#4169E1',  
            'accepted': '#228B22',  
            'rejected': '#DC143C',  
        }
        color = colors.get(obj.application_status, '#808080')
        return format_html(
            '<span style="background-color: {}; color: white; padding: 5px 10px; '
            'border-radius: 3px; font-weight: bold;">{}</span>',
            color,
            obj.get_application_status_display(),
        )
    status_badge.short_description = 'Status'

    def mark_as_reviewed(self, request, queryset):
        """Bulk action to mark applications as reviewed."""
        updated = queryset.update(application_status='reviewed')
        self.message_user(request, f'{updated} application(s) marked as reviewed.')
    mark_as_reviewed.short_description = "Mark selected as Reviewed"

    def mark_as_accepted(self, request, queryset):
        """Bulk action to mark applications as accepted."""
        updated = queryset.update(application_status='accepted')
        self.message_user(request, f'{updated} application(s) marked as accepted.')
    mark_as_accepted.short_description = "Mark selected as Accepted"

    def mark_as_rejected(self, request, queryset):
        """Bulk action to mark applications as rejected."""
        updated = queryset.update(application_status='rejected')
        self.message_user(request, f'{updated} application(s) marked as rejected.')
    mark_as_rejected.short_description = "Mark selected as Rejected"
