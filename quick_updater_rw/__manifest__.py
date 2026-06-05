# -*- coding: utf-8 -*-
{
    'name': 'Quick Updater RW',
    'version': '17.0.1.0.1',
    'category': 'Technical',
    'summary': 'Actualizador rápido de módulos compatible con responsive_web',
    'description': """
Quick Updater RW
========================

Este módulo añade un widget de actualización rápida en la barra superior de Odoo 17
adaptado para convivir con responsive_web.

Características principales:
----------------------------
* Widget dropdown en la barra superior para actualizar módulos
* Lista de todos los módulos instalados
* Agrega los módulos a favoritos
* Muestra siempre los módulos favoritos primero
* Actualización con un solo clic
* Notificaciones de éxito/error
* Búsqueda y filtros rápidos

Desarrollado por: Duvan
    """,
    'author': 'DZ Development',
    'website': '',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'web',
        'responsive_web',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/update_log_views.xml',
        'data/ir_cron.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'quick_updater_rw/static/src/components/module_updater/module_updater.js',
            'quick_updater_rw/static/src/components/module_updater/module_updater.xml',
            'quick_updater_rw/static/src/components/module_updater/module_updater.scss',
        ],
    },
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': False,
    'auto_install': False,
}
