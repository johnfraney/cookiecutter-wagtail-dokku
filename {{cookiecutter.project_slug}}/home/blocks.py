from wagtail.wagtailcore import blocks
from wagtail.wagtailimages.blocks import ImageChooserBlock


class SectionBlock(blocks.StructBlock):
    content = blocks.RichTextBlock()
    margins = blocks.ChoiceBlock(
        choices=[
            ('default', 'Comfortable'),
            ('small', 'Small'),
            ('flush', 'None'),
        ],
        default='default',
        help_text="Size of this section's top/bottom margins",
    )
    background_colour = blocks.ChoiceBlock(
        choices=[
            ('white', 'White'),
            ('black', 'Black'),
            ('faded', 'Faded'),
        ],
        default='white',
        help_text="The background colour of this section"
    )

    class Meta:
        template = 'blocks/section_block.html'


class CallToActionBlock(blocks.StructBlock):
    content = blocks.RichTextBlock(required=False)
    link_text = blocks.CharBlock(help_text="Text that appears in the button")
    url = blocks.URLBlock()
    background_colour = blocks.ChoiceBlock(
        choices=[
            ('white', 'White'),
            ('primary', 'Primary'),
            ('success', 'Success'),
            ('info', 'Info'),
            ('warning', 'Warning'),
            ('danger', 'Danger'),
            ('inverse', 'Black'),
        ],
        default='white',
        help_text="The background colour of this section"
    )
    button_colour = blocks.ChoiceBlock(
        choices=[
            ('primary', 'Primary'),
            ('secondary', 'Secondary'),
            ('success', 'Success'),
            ('info', 'Info'),
            ('warning', 'Warning'),
            ('danger', 'Danger'),
        ],
        default='pimary',
    )

    class Meta:
        template = 'blocks/call_to_action_block.html'


class PullQuoteBlock(blocks.StructBlock):
    quote = blocks.TextBlock("quote title")
    attribution = blocks.CharBlock()

    class Meta:
        icon = "openquote"


class ImageTextBlock(blocks.StructBlock):
    image = ImageChooserBlock()
    text = blocks.RichTextBlock()

    class Meta:
        icon = "image"


class ButtonBlock(blocks.StructBlock):
    text = blocks.CharBlock()

    SIZE_CHOICES = (
        ('small', 'Small'),
        ('regular', 'Regular'),
        ('large', 'Large'),
        ('xlarge', 'Extra Large'),
    )
    size = blocks.ChoiceBlock(choices=SIZE_CHOICES, default='regular')
    colour = None

    class Meta:
        icon = "radio-full"
        template = 'blocks/button.html'
