from django.contrib import admin

# Register your models here.
from django.utils.safestring import mark_safe

from photos.models import Photo



class PhotoAdmin(admin.ModelAdmin):
    list_display = ('name', 'license', 'owner_name', 'visibility')
    list_filter = ('license', 'visibility')
    search_fields = ('name', 'description')
    readonly_fields = ('image_tag',)

    fieldsets = (
        ("Name and Description", {
            'fields': ('name', 'description'),
            'classes': ('wide',)
        }),
        ('Author', {
            'fields': ('owner',),
            'classes': ('wide',)
        }),
        ('URL', {
            'fields': ('url', 'image_tag',),
            'classes': ('wide',)
        }),
        ('License and visibility', {
            'fields': ('license', 'visibility',),
            'classes': ('wide', 'collapse')  # clase colapse para ocultar y mostrar los campos.
        }),
    )


    # personalizamos el campo de propietario para que muestre el nombre completo y no usuario.

    def owner_name(self, photo):
        return "{0} {1}".format(photo.owner.first_name, photo.owner.last_name)

    owner_name.admin_order_field = "owner"
    owner_name.short_description = "Propietario"

    def image_tag(self, photo):
        return mark_safe("<img src={0}>".format(photo.url))


admin.site.register(Photo, PhotoAdmin)

