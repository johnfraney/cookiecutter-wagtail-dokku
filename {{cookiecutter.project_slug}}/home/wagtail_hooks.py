from django.contrib.staticfiles.templatetags.staticfiles import static
from django.utils.html import format_html, format_html_join
from django.conf import settings

from wagtail.wagtailcore import hooks
from wagtail.wagtailcore.whitelist import attribute_rule, check_url, allow_without_attributes


@hooks.register('insert_editor_css')
def editor_css():
    return format_html(
        '<link rel="stylesheet" href="{}">',
        static('css/wagtail-justify-icons.css')
    )


@hooks.register('construct_whitelister_element_rules')
def whitelister_element_rules():
    return {
        'p': attribute_rule({'class': True, 'align': True}),
        'h1': attribute_rule({'class': True, 'align': True}),
        'h2': attribute_rule({'class': True, 'align': True}),
        'h3': attribute_rule({'class': True, 'align': True}),
        'h4': attribute_rule({'class': True, 'align': True}),
    }


@hooks.register('insert_editor_js')
def editor_js():
    return format_html(
        """
        <script>
            registerHalloPlugin('hallojustify');
        </script>
        """
    )
