from __future__ import absolute_import, unicode_literals

from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.wagtailcore.fields import StreamField, RichTextField
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore import blocks
from wagtail.wagtailadmin.edit_handlers import (
    FieldPanel, InlinePanel, MultiFieldPanel, StreamFieldPanel)
from wagtail.wagtailforms.models import AbstractEmailForm, AbstractFormField
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel

from .blocks import CallToActionBlock, ImageTextBlock, PullQuoteBlock, SectionBlock


class StandardPage(Page):
    feature_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    feature_image_large = models.BooleanField(default=False)
    body = StreamField([
        ('heading', blocks.CharBlock(
            classname='full title', template='blocks/heading.html')),
        ('section', SectionBlock()),
        ('image', ImageTextBlock(template='blocks/image_text.html')),
        ('quote', PullQuoteBlock(template='blocks/quote.html')),
        ('call_to_action', CallToActionBlock()),
    ])

    content_panels = Page.content_panels + [
        ImageChooserPanel('feature_image'),
        FieldPanel('feature_image_large'),
        FieldPanel('feature_text'),
        StreamFieldPanel('body'),
    ]


class FormField(AbstractFormField):
    page = ParentalKey('FormPage', related_name='form_fields')


class FormPage(AbstractEmailForm):
    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel('intro', classname='full'),
        InlinePanel('form_fields', label='Form fields'),
        FieldPanel('thank_you_text', classname='full'),
        MultiFieldPanel([
            FieldPanel('to_address', classname='full'),
            FieldPanel('from_address', classname='full'),
            FieldPanel('subject', classname='full'),
        ], 'Email')
    ]
