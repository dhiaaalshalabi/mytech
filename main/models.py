from django.core.validators import FileExtensionValidator, MaxLengthValidator, MinLengthValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class SiteLogo(models.Model):
    name = models.CharField(max_length=15, verbose_name=_('Site Title'))
    logo = models.FileField(
        verbose_name=_('Site Logo'),
        upload_to='main/',
        validators=[FileExtensionValidator(
            allowed_extensions=['svg', 'png', 'jpg'])],
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = _('Site Logo')


class Carousel(models.Model):
    image = models.ImageField(
        verbose_name=_('Carousel Image'),
        upload_to='carousel/',
        blank=True,
        null=True
    )
    title = models.CharField(max_length=50, verbose_name=_("Title"))
    description = models.TextField(
        verbose_name=_("Description"),
        validators=[MaxLengthValidator(500)]
    )
    enabled = models.BooleanField(default=True, verbose_name=_("Enabled"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = _('Carousel')


class CarouselAction(models.Model):
    carousel = models.ForeignKey(Carousel, on_delete=models.CASCADE)
    label = models.CharField(max_length=10, verbose_name=_('Label'))
    BUTTON = [
        ('danger', _('Red')),
        ('primary', _('Blue')),
        ('warning', _('Yellow')),
        ('dark ', _('Dark'))
    ]
    button = models.CharField(
        max_length=20,
        verbose_name=_('Button'),
        choices=BUTTON,
        default='primary'
    )
    action = models.URLField(verbose_name=_('Action'))
    outline = models.BooleanField(default=True, verbose_name=_('Outline'))
    enabled = models.BooleanField(default=True, verbose_name=_('Enabled'))

    def __str__(self):
        return self.label

    class Meta:
        verbose_name_plural = _('Carousel Action')


class SiteSection(models.Model):
    TYPE_CHOICES = [('why_chose', _('Why Chose'))]
    section_type = models.CharField(max_length=50, choices=TYPE_CHOICES, verbose_name=_('Section Type'))
    name = models.CharField(max_length=20, verbose_name=_('Name'))
    label = models.CharField(max_length=20, verbose_name=_('Label'))
    description = models.TextField(
        verbose_name=_('Description'),
        validators=[MinLengthValidator(70), MaxLengthValidator(100)],
        blank=True,
        null=True
    )
    enabled = models.BooleanField(default=True, verbose_name=_('Enabled'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = _('Site Section')


class WhyChose(models.Model):
    title = models.CharField(max_length=50, verbose_name=_('Title'))
    description = models.TextField(
        verbose_name=_('Description'),
        validators=[MinLengthValidator(70), MaxLengthValidator(110)]
    )
    icon = models.ImageField(upload_to='whychose/', verbose_name=_('Icon'), blank=True, null=True)
    enabled = models.BooleanField(default=True, verbose_name=_('Enabled'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = _('Why Chose')


class AboutUsMessage(models.Model):
    label = models.CharField(max_length=30, verbose_name=_('Label'))
    description = models.TextField(validators=[MinLengthValidator(70), MaxLengthValidator(110)])
    image = models.ImageField(verbose_name=_('Image'), upload_to='aboutus/')
    enabled = models.BooleanField(default=True, verbose_name=_('Enabled'))

    def __str__(self):
        return self.label

    class Meta:
        verbose_name_plural = _('About Us Message')


class MessagePoint(models.Model):
    label = models.CharField(max_length=15, verbose_name=_('Label'))
    title = models.CharField(max_length=50, verbose_name=_('Title'))
    description = models.TextField(validators=[MinLengthValidator(40), MaxLengthValidator(60)])

    def __str__(self):
        return self.label

    class Meta:
        verbose_name_plural = _('Message Point')
