from datetime import timedelta
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class AlquilerProducto(models.Model):
    _name='alquiler.producto'
    _description='Gestión de Alquiler de Productos'

    cliente = fields.Many2one('res.partner', string='Cliente', store=True, required=True)
    producto = fields.Many2one('product.product', string='Producto', store=True, required=True)
    fecha_inicio = fields.Date(string='Fecha de Inicio del Alquiler', required=True)
    
    fecha_final = fields.Date(
        string='Fecha del Final del Alquiler', 
        compute='_compute_fecha_final',
        store=True,
        readonly=True
    )
    
    estado = fields.Selection([
        ('en_alquiler', 'En alquiler'),
        ('entregado', 'Entregado'),
        ('no_entregado', 'No entregado')
    ], string='Estado', required=True, default='en_alquiler')
    
    observaciones = fields.Text(string='Observaciones')

    @api.depends('fecha_inicio')
    def _compute_fecha_final(self):
        for i in self:
            if i.fecha_inicio:
                i.fecha_final = i.fecha_inicio + timedelta(days=30)
            else:
                i.fecha_final = False

    @api.onchange('producto')
    def comprobar_producto(self):
        if self.producto:
            product = self.env['product.product'].browse(self.producto.id)
            if not product.exists():
                raise ValidationError('El producto seleccionado no existe')
            
    @api.model
    def cambiar_estado_alquiler(self):
        hoy = fields.Date.today()
        alquileres = self.search([('fecha_final', '<', hoy), ('estado', '!=', 'entregado')])
        for alquiler in alquileres:
            alquiler.estado = 'no_entregado'