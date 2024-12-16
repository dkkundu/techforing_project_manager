from django.contrib import admin
from .models import User, Project, ProjectMember, Task, Comment

# Register User Model
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'date_joined')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('date_joined',)

# Register Project Model
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'owner', 'created_at')
    search_fields = ('name', 'owner__username')
    list_filter = ('created_at',)
    ordering = ('-created_at',)

# Register ProjectMember Model
@admin.register(ProjectMember)
class ProjectMemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'project', 'user', 'role')
    search_fields = ('project__name', 'user__username', 'role')
    list_filter = ('role',)

# Register Task Model
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'priority', 'assigned_to', 'project', 'created_at', 'due_date')
    search_fields = ('title', 'assigned_to__username', 'project__name')
    list_filter = ('status', 'priority', 'created_at', 'due_date')
    ordering = ('-created_at',)

# Register Comment Model
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'user', 'task', 'created_at')
    search_fields = ('content', 'user__username', 'task__title')
    list_filter = ('created_at',)
    ordering = ('-created_at',)
