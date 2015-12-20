from django.contrib import admin

from .models import User, UserLogin, Report, Torrent, Tag, TorrentTag

class LoginInline(admin.TabularInline):
    model = UserLogin
    extra = 0

class ReportInline(admin.TabularInline):
    model = Report
    extra = 0

class UserAdmin(admin.ModelAdmin):
    list_display = [
            'username', 
            'email',  
            'joined_date', 
            'member_type',
            'uploaded',
            'downloaded',
            'torrents_uploaded',
            'invites'
    ]

    search_fields = ['username', 'email', 'passkey', 'member_type'] 

    inlines = [LoginInline, ReportInline]

class UserLoginAdmin(admin.ModelAdmin):
    list_display = ['user', 'login', 'ip']
    search_fields = ['user', 'ip']

class TagInline(admin.TabularInline): 
    model = TorrentTag
    extra = 0

class TorrentAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'description',
        'date_uploaded',
        'uploader',
        'size',
        'downloads',
        'seeders',
        'leechers'
    ]
    
    search_fields = ['title', 'description', 'uploader']
    
    inlines = [TagInline, ReportInline]

class ReportAdmin(admin.ModelAdmin):
    list_display = ['reporter', 'reported_torrent', 'reason']
    search_fields = ['reporter', 'reported_torrent']

class TagAdmin(admin.ModelAdmin):
    list_display = ['creator', 'tag']
    search_fields = ['creator', 'tag']

admin.site.register(User, UserAdmin)
admin.site.register(UserLogin, UserLoginAdmin)
admin.site.register(Torrent, TorrentAdmin)
admin.site.register(Report, ReportAdmin)
admin.site.register(Tag, TagAdmin)
