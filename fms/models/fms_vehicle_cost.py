from datetime import datetime

from odoo import api, fields, models

class FleetVehicleCost(models.Model):
	_inherit = 'fleet.vehicle.cost'

	quantity= fields.Float('Quantity')
	name = fields.Many2one('product.template', 'Type', help='Cost type purchased with this cost')

	@api.onchange('name')
	def on_cost_subtype_id_change(self):
		if self.name.category == 'contract':
			# contract = {
			# 	'name': x.vehicle_id.id,
			# 	'date': self.date,
			# 	'route': self.route.id,
			# 	'client': self.client.id,
			# 	'total': total_sale
			# }
			# self.env['fleet.sale'].create(fleet_sale)
			print 'contract'
		if self.name.category == 'service':
			# service = {
			# 	'name': x.vehicle_id.id,
			# 	'date': self.date,
			# 	'route': self.route.id,
			# 	'client': self.client.id,
			# 	'total': total_sale
			# }
			# self.env['fleet.sale'].create(service)
			print 'service'
		if self.name.category == 'other':
			# move_line = {}
			# picking_type = {}
			# picking_type[0] = 6
			# # picking_type[1] = 14
			# move_line[0] = 14
			# move_line[1] = 15
			# for product in prod(1,10):
			# 	pass
			# move_lines_item ={
			# 	'name': self.name.name,
			# 	'product_id': self.name.id,
			# 	'product_tmpl_id': self.name.id,
			# 	'ordered_qty': self.quantity,
			# 	'product_uom_qty': self.quantity,
			# 	'product_uom': 1,
			# 	'location_id': 15,
			# 	'location_dest_id': 18,
			# 	'state': 'done',

			# }
			# print move_lines_item
			# sm = self.env['stock.move'].create(move_lines_item)

			# stock_picking = {
			# 	'move_type': 'one',
			# 	'picking_type_id': 6,
			# 	'location_id': 15,
			# 	'location_dest_id': 18,
			# 	'move_lines': [sm],
			# }
			# self.env['stock.picking'].create(stock_picking)
			print 'other'

	@api.model
	def create(self, values):
		return super(FleetVehicleCost, self).create(values)