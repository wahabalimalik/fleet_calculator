from datetime import datetime

from odoo import api, fields, models

class FleetSale(models.Model):
	_name = 'fleet.sale'
	_description = "Fleet Sale"

	name = fields.Many2one('tms.unit.kit')
	route = fields.Many2one('fleet.vehicle.route')
	client = fields.Many2one('res.partner')
	rate = fields.Float()
	date = fields.Date()
	total = fields.Float()
