from django.contrib import admin

from main.models import CarouselAction, Carousel, SiteLogo, SiteSection, WhyChose

admin.site.site_header = 'MY-TECH Administration'


class CarouseActionInline(admin.TabularInline):
    model = CarouselAction
    extra = 1
    max_num = 3


class CarouselAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'enabled']
    inlines = [CarouseActionInline]


admin.site.register(Carousel, CarouselAdmin)


class SiteLogoAdmin(admin.ModelAdmin):
    list_display = ['name']

    def save_model(self, request, obj, form, change):
        obj.id = 1
        return super().save_model(request, obj, form, change)


admin.site.register(SiteLogo, SiteLogoAdmin)


class SiteSectionAdmin(admin.ModelAdmin):
    list_display = ['section_type', 'name', 'label', 'description', 'enabled']


admin.site.register(SiteSection, SiteSectionAdmin)


class WhyChoseAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'enabled']


admin.site.register(WhyChose, WhyChoseAdmin)
