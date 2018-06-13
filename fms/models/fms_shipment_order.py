from datetime import datetime

from odoo import api, fields, models

class ShipmentDescription(models.Model):
	_name = 'shipment.description'
	name = fields.Char('Description Name')
	_description = "Shipment Description"

class ShipmentVehicle(models.Model):
	_name = 'shipment.order.vehicle'
	_description = "Shipment Order Vehicle"

	vehicle_id = fields.Many2one('tms.unit.kit','Vehicle')
	cost_sub_total = fields.Float('Cost Subtotal', readonly = True)
	vehicle_shipment_id = fields.Many2one('shipment.order')
	revenue_sub_total = fields.Float('Revenue Subtotal')

class ShipmentOrder(models.Model):
	_name = 'shipment.order'
	_description = "Shipment Order"


	date = fields.Date()
	name = fields.Char('Shipment Order No.')
	route = fields.Many2one('fleet.vehicle.route')
	client = fields.Many2one('res.partner')
	description = fields.Many2one('shipment.description')
	vehicle_ids = fields.One2many('shipment.order.vehicle','vehicle_shipment_id')
	total_cost = fields.Float( compute='_compute_total_cost',string="Total Cost", readonly = True,  store = True)
	total_revenue = fields.Float( compute='_compute_total_cost',string="Total Revenue", readonly = True,  store = True)
	total_distance = fields.Float( compute='_compute_total_cost',string="Total Distance", readonly = True,  store = True)
	bool_field = fields.Boolean()

	no_trucks =fields.Float()
	status =fields.Char()

	@api.onchange('vehicle_ids')
	def on_vehicle_ids_change(self):
		for x in self.vehicle_ids:
			x.cost_sub_total = self.route.total_route_cost
			x.update({'cost_sub_total' : self.route.total_route_cost})

	
	@api.multi
	def _compute_total_cost(self):
		n = 0


	@api.multi
	def action_confirm(self):
		client_id = self.client.id
		self.bool_field = True
		fuel_unit_price = 90.0
		fuel_cost = 80.0
		total_route_cost = 0.0
		total_expense = 0.0

		for client in self.route.route_client_id:
			if client.client_id.id == self.client.id:
				total_sale = client.price

		for route_cost in self.route.route_cost_id:
			total_route_cost = total_route_cost + route_cost.cost
			if route_cost.name.category == 'fuel':
				fuel_unit_price = route_cost.unit_price
				fuel_cost = route_cost.cost

		for x in self.vehicle_ids:
			total_expense = total_expense + total_route_cost
			#create a sale for each vehicle
			fleet_sale = {
				'name': x.vehicle_id.id,
				'date': self.date,
				'route': self.route.id,
				'client': self.client.id,
				'total': total_sale
			}
			self.env['fleet.sale'].create(fleet_sale)

			#create a fuel voucher for each vehicle()
			#get fuel type and price product.template
			fuel_voucher = { 						
				'date': datetime.now(),
				'operating_unit_id': 1, 
				'vehicle_id': x.vehicle_id.unit_id.id,
				'product_qty': self.route.total_fuel,
				'price_unit': fuel_unit_price,
				'price_subtotal': fuel_cost,
				'vendor_id': 1,
				'product_id': 12
				}
			self.env['fleet.vehicle.log.fuel'].create(fuel_voucher)

			for y in self.route.route_cost_id:
				# if y.name.id != False:
				unit_cost = { 						
					'date': datetime.now(),
					'name': y.name.id, 
					'vehicle_id': x.vehicle_id.unit_id.id,
					'amount': y.cost
				}
				self.env['fleet.vehicle.expense'].create(unit_cost)

		# self.update = {
		# 	'total_cost' = total_expense,
		# 	'total_revenue' = total_sale,
		# }
		self.update({
			'total_cost': total_expense,
			'total_revenue': total_sale,
		})
		hr_expense = {
			'name': u'Expense for Shipment Order : %s' %(self.name), 
			'product_id': self.route.route_product_id.id, 
			'unit_amount': total_expense
		}
		self.env['hr.expense'].create(hr_expense)

		# sale_order = {
		# 	'partner_id': self.client.id,
		# 	'state': 'sale',
		# 	'amount_untaxed': 54654.54,
		# 	'amount_total':  9829.09
		# }
		# self.env['sale.order'].create(sale_order)

