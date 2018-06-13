# -*- coding: utf-8 -*-

from datetime import datetime

from odoo import api, fields, models

class FuelTanker(models.Model):
	_name = 'fuel.tanker'
	_description = "Tanker"

	name = fields.Char()
	total_fuel_level = fields.Float(string='Total Size')
	fuel_type = fields.Char(string='Fuel Type')

class FuelTankerFillup(models.Model):
	_name = 'fuel.tanker.log'
	_description = "Fuel Tanker Log"

	date = fields.Datetime(string='Date')
	reading_before = fields.Float(string='Opening Inventory')
	reading_after = fields.Float(string='Closing Inventory', compute='_compute_closing')
	fuel_deliver = fields.Float(string='Fuel Deliver')
	fuel_issue = fields.Float(string='Fuel Issue')
	name = fields.Many2one('fuel.tanker', 'Tanker')
	is_done = fields.Boolean(default=False)
	fuelled_amount = fields.Float(string='Total Fuel')
	total_fuel = fields.Float('Total In Tanker')
	pump_id = fields.Many2one(string='fuel.tanker.pump')
	operator_id = fields.Many2one('hr.employee', string='Receiver')
	operation_type = fields.Selection([('fuel_stocking','Fuel Stocking'),('fuel_consuming','Fuel Consuming'),('others','Others')])
	fuel_discrepancy = fields.Char('Discrepancy',compute='_compute_discrepancy', store=True)
	fuel_in_tanker = fields.Float('Fuel In Stock',compute='_compute_discrepancy')
	
	@api.depends('reading_after','fuel_issue','fuel_deliver')
	def _compute_closing(self):
		for x in self:
			x.reading_after = x.reading_before - (x.fuel_issue if x.fuel_issue else 0) + (x.fuel_deliver if x.fuel_deliver else 0)

	@api.multi
	def _compute_discrepancy(self):
		self.fuel_in_tanker = 0.0
		fuel_amount = self.reading_after - self.reading_before
		self.fuel_discrepancy = fuel_amount - self.fuelled_amount
		self.total_fuel = fuel_amount
		f = self.env['fuel.tanker.log'].search([])
		for fuel in f:
			self.fuel_in_tanker = self.fuel_in_tanker + fuel.total_fuel

	@api.onchange('tanker')
	def on_reading_after_change(self):
		self.fuel_in_tanker = 0.0
		f = self.env['fuel.tanker.log'].search([])
		for fuel in f:
			self.fuel_in_tanker = self.fuel_in_tanker + fuel.total_fuel

	@api.onchange('reading_after')
	def on_tanker_id_change(self):
		self.fuel_in_tanker = 0.0
		fuel_amount = self.reading_after - self.reading_before
		self.fuel_discrepancy = fuel_amount - self.fuelled_amount
		self.total_fuel = fuel_amount
		f = self.env['fuel.tanker.log'].search([])
		for fuel in f:
			self.fuel_in_tanker = self.fuel_in_tanker + fuel.total_fuel

	@api.multi
	def action_confirm(self):
		self.fuel_in_tanker = 0.0
		self.is_done = True
		fuel_amount = self.reading_after - self.reading_before
		self.fuel_discrepancy = fuel_amount - self.fuelled_amount
		self.total_fuel = fuel_amount
		f = self.env['fuel.tanker.log'].search([])
		for fuel in f:
			self.fuel_in_tanker =+ fuel.total_fuel

class FuelTankerVehicleFillup(models.Model):
	_name = 'fuel.tanker.vehicle.log'
	_description = "Vehicle Fuel"

	name = fields.Many2one('fleet.vehicle.log.fuel','Voucher No.')
	tanker_id = fields.Many2one('fuel.tanker','Tanker No.')
	driver_id = fields.Many2one('hr.employee', string="Driver")
	operator_id = fields.Many2one('hr.employee', string="Receiver")
	pump_id = fields.Many2one('fuel.tanker.pump', string="Pump No.")
	date = fields.Datetime('Fueled Date')
	reading_before = fields.Float(string='Opening Inventory')
	reading_after = fields.Float(string='Closing Inventory')
	fuel_issue = fields.Float(string='Fuel Issue')
	is_done = fields.Boolean(default=False)
	fuel_discrepancy = fields.Char('Discrepancy',compute='_compute_discrepancy', store=True)
	fuel_in_tanker = fields.Float('Fuel In Stock',compute='_compute_discrepancy')
	total_fuel_voucher = fields.Float('Fuel In Voucher',compute='_compute_discrepancy')

	@api.onchange('name')
	def on_name_change(self):
		self.fuel_in_tanker = 0.0
		self.total_fuel_voucher = self.name.product_qty
		fuel_amount = self.reading_after - self.reading_before
		self.fuel_discrepancy = fuel_amount - self.total_fuel_voucher
		# self.total_fuel = fuel_amount
		f = self.env['fuel.tanker.log'].search([])
		for fuel in f:
			self.fuel_in_tanker = self.fuel_in_tanker + fuel.total_fuel

	@api.multi
	def _compute_discrepancy(self):
		self.fuel_in_tanker = 0.0
		self.total_fuel_voucher = self.name.product_qty
		fuel_amount = self.reading_after - self.reading_before
		self.fuel_discrepancy = fuel_amount - self.total_fuel_voucher
		# self.total_fuel = fuel_amount
		f = self.env['fuel.tanker.log'].search([])
		for fuel in f:
			self.fuel_in_tanker = self.fuel_in_tanker + fuel.total_fuel

	@api.onchange('reading_after')
	def on_reading_after_change(self):
		self.fuel_in_tanker = 0.0
		self.total_fuel_voucher = self.name.product_qty
		fuel_amount = self.reading_after - self.reading_before
		self.fuel_discrepancy = fuel_amount - self.total_fuel_voucher
		# self.total_fuel = fuel_amount
		f = self.env['fuel.tanker.log'].search([])
		for fuel in f:
			self.fuel_in_tanker = self.fuel_in_tanker + fuel.total_fuel

	@api.onchange('reading_before')
	def on_reading_before_change(self):
		self.fuel_in_tanker = 0.0
		self.total_fuel_voucher = self.name.product_qty
		fuel_amount = self.reading_after - self.reading_before
		self.fuel_discrepancy = fuel_amount - self.total_fuel_voucher
		# self.total_fuel = fuel_amount
		f = self.env['fuel.tanker.log'].search([])
		for fuel in f:
			self.fuel_in_tanker = self.fuel_in_tanker + fuel.total_fuel

	@api.multi
	def action_confirm(self):
		self.fuel_in_tanker = 0.0
		self.total_fuel_voucher = self.name.product_qty
		self.is_done = True
		vars = {}
		vars['is_filled'] = True
		self.name.is_filled = True
		fuel_amount = self.reading_after - self.reading_before
		self.fuel_discrepancy = fuel_amount - self.total_fuel_voucher
		fuel_tanker_log = {
			'name' :  self.tanker_id.id,
			'is_done' :  True,
			'fuelled_amount' :  -(self.total_fuel_voucher),
			'total_fuel' : -(fuel_amount) ,
			# 'pump_id' : self.pump_id ,
			'date' :  datetime.now(),
			# 'operator_id' :  self.operator_id,
			'reading_after' :  self.reading_after,
			'reading_before' :  self.reading_before,
			'operation_type' :  'fuel_consuming',
			'fuel_discrepancy' : self.fuel_discrepancy,
		}
		self.env['fuel.tanker.log'].create(fuel_tanker_log)
		f = self.env['fuel.tanker.log'].search([])
		for fuel in f:
			self.fuel_in_tanker = self.fuel_in_tanker + fuel.total_fuel

class FuelTankerVehicleFillup(models.Model):
	_name = 'fuel.tanker.pump'
	_description = "Pump"

	name = fields.Char('Pump Name')
	current_odometer = fields.Float('Current odometer')
	past_odometer = fields.Float('Past odometer')
	past_odometer_date = fields.Datetime('Past Date')
	operator_id = fields.Many2one('res.partner', string="Operator")

class FleetVehicleLogFuel(models.Model):
    # _name = 'fleet.vehicle.log.fuel'
    _inherit = 'fleet.vehicle.log.fuel'

    name = fields.Char('Voucher No.',compute='_compute_vehicle_log_fuel_voucher_no', store=True)
    # vehicle_id = fields.Many2one('fleet.vehicle','Vehicle')

    @api.depends('vehicle_id')
    def _compute_vehicle_log_fuel_voucher_no(self):
        for record in self:
            name = record.vehicle_id.name
            t = str(datetime.now())
            if not name:
                name = t
            elif t:
                name += ""
            self.name = name

class FualActual(models.Model):
	_name = 'tanker.physical'

	opening_reading = fields.Float()
	closing_reading = fields.Float()
	balence = fields.Float()
	Variance = fields.Float()