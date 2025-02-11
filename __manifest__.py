{
'name': 'Alquiler de Productos',
'version': '1.0',
'author': 'Miguel Ángel Bernal Sánchez',
'category': 'Custom',
'summary': 'Gestión de Alquiler de productos',
'depends': ['base'],
'data': [
    'security/ir.model.access.csv',
    'views/alquiler_producto_views.xml',
],
    'icon': '/alquiler_producto/static/description/icon56.png',
    'installable': True,
    'application': True,
}