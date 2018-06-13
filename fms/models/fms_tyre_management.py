# -*- coding: utf-8 -*-

from odoo import api, fields, models

class FmsTyre(models.Model):
	_name = 'fms.tyre'
	_description = "Tyre Management"

	fitment_date = fields.Date()
	vehicle_id = fields.Many2one('fleet.vehicle','Vehicle', required=True)
	vehicle_number = fields.Char('Vehicle Number', related="vehicle_id.license_plate" )
	tyre_size = fields.Char()
	tyre_make = fields.Many2one('tyre.make')
	tyre_model = fields.Many2one('tyre.model')
	position_fitted = fields.Char()
	serial_number = fields.Char()
	reading = fields.Float()
	driver_id = fields.Many2one('res.partner', string="Driver")
	total_tyre = fields.Integer()
	remaining_stock = fields.Integer()


class TyreMake(models.Model):
	_name = 'tyre.make'

	name = fields.Char()

class TyreModel(models.Model):
	_name = 'tyre.model'

	name = fields.Char()