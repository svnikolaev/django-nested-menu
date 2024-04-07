from django.contrib import admin
from .models import MenuItem


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'parent', 'menu_name']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "parent" and request._obj_ is not None:
            kwargs["queryset"] = MenuItem.objects.filter(menu_name=request._obj_.menu_name).exclude(id=request._obj_.id)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def get_form(self, request, obj=None, **kwargs):
        request._obj_ = obj
        return super(MenuItemAdmin, self).get_form(request, obj, **kwargs)
