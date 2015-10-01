# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template.loader import select_template
from django.utils.translation import ugettext_lazy as _
from cms.plugin_pool import plugin_pool
from shop import settings as shop_settings
from .plugin_base import ShopPluginBase


class ShopOrderViewsPlugin(ShopPluginBase):
    name = _("Order Views")
    require_parent = True
    parent_classes = ('BootstrapColumnPlugin',)
    cache = False

    def get_render_template(self, context, instance, placeholder):
        many = context.get('many')
        if many is True:
            # render Order List View
            template_names = [
                '{}/order/list.html'.format(shop_settings.APP_LABEL),
                'shop/order/list.html',
            ]
        elif many is False:
            # render Order Detail View
            template_names = [
                '{}/order/detail.html'.format(shop_settings.APP_LABEL),
                'shop/order/detail.html',
            ]
        else:
            # can happen, if this plugin is abused outside of an OrderView
            template_names = ['cascade/generic/naked.html']
        return select_template(template_names)

plugin_pool.register_plugin(ShopOrderViewsPlugin)