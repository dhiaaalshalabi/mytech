from main.models import SiteLogo, SiteSection


def site_context(request):
    logo = SiteLogo.objects.first()
    site_sections = SiteSection.objects.filter(enabled=True)
    site_sections_dict = dict()
    for section in site_sections:
        site_sections_dict[section.section_type] = section
    return {'site_logo': logo, 'site_sections': site_sections_dict}
