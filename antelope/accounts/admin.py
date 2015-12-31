from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import AntelopeUser, UserLogin

class UserLoginInline(admin.TabularInline):
    model = UserLogin
    extra = 0

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = AntelopeUser
        fields = ('username', 'email')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")

        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])

        if commit:
            user.save()

        return user

class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = AntelopeUser
        fields = (
            'username',
            'password',
            'email', 
            'passkey',
            'is_active',
            'is_admin',
            'uploaded',
            'downloaded',
            'torrents_uploaded',
            'torrents_downloaded',
            'invites',
            'can_invite',
        )

    def clean_password(self):
        return self.initial["password"]

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('username', 'email', 'passkey')
    list_filter = ('is_admin', 'is_active', 'can_invite',)
    fieldsets = (
        (None, {'fields': ('username', 'email', 'passkey', 'invites', 'password',)}), 
        ('Permissions', {'fields': ('is_active', 'can_invite', 'is_admin',)}),
        ('Torrents', {'fields': ('torrents_uploaded', 'torrents_downloaded', 'uploaded', 'downloaded',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2')}
        ),        
    )
    search_fields = ('username', 'email', 'passkey',)
    ordering = ('username',)
    filter_horizontal = ()

    inlines = [UserLoginInline]

class UserLoginAdmin(admin.ModelAdmin):
    list_display = ('user', 'login', 'ip')
    search_fields = ('user', 'ip',' login')

admin.site.register(AntelopeUser, UserAdmin)
admin.site.register(UserLogin, UserLoginAdmin)
admin.site.unregister(Group)
