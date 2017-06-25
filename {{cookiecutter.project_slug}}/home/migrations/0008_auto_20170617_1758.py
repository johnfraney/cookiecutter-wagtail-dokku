# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-17 21:58
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20170617_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title', template='blocks/heading.html')), ('section', wagtail.wagtailcore.blocks.StructBlock((('content', wagtail.wagtailcore.blocks.RichTextBlock()), ('margins', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('default', 'Comfortable'), ('small', 'Small'), ('flush', 'None')], help_text="Size of this section's top/bottom margins")), ('background_colour', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('black', 'Black'), ('faded', 'Faded')], help_text='The background colour of this section (defaults to white)', required=False))))), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('text', wagtail.wagtailcore.blocks.RichTextBlock())), template='blocks/image_text.html')), ('quote', wagtail.wagtailcore.blocks.StructBlock((('quote', wagtail.wagtailcore.blocks.TextBlock('quote title')), ('attribution', wagtail.wagtailcore.blocks.CharBlock())), template='blocks/quote.html')))),
        ),
        migrations.AlterField(
            model_name='standardpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title', template='blocks/heading.html')), ('section', wagtail.wagtailcore.blocks.StructBlock((('content', wagtail.wagtailcore.blocks.RichTextBlock()), ('margins', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('default', 'Comfortable'), ('small', 'Small'), ('flush', 'None')], help_text="Size of this section's top/bottom margins")), ('background_colour', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('black', 'Black'), ('faded', 'Faded')], help_text='The background colour of this section (defaults to white)', required=False))))), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('text', wagtail.wagtailcore.blocks.RichTextBlock())), template='blocks/image_text.html')), ('quote', wagtail.wagtailcore.blocks.StructBlock((('quote', wagtail.wagtailcore.blocks.TextBlock('quote title')), ('attribution', wagtail.wagtailcore.blocks.CharBlock())), template='blocks/quote.html')))),
        ),
    ]