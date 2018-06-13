# -*- coding: utf-8 -*-
from odoo import api, fields, models


class FleetVehicleAccident(models.Model):
    _name = 'fleet.vehicle.accident'
    _description = "Vehicle Accident"

    date = fields.Date(required=True)
    vehicle_id = fields.Many2one('fleet.vehicle','Vehicle')
    vehicle_number = fields.Char('Vehicle Number',related="vehicle_id.license_plate" )
    trailor_id = fields.Many2one('fleet.trailor','Trailor Number')
    employee_id = fields.Many2one( 'hr.employee', string="Driver", domain=[('driver', '=', True)])
    location = fields.Char()
    accident_report = fields.Text('Accident Report')
    damage_cause = fields.Many2many('damage.cause')

class DemageCause(models.Model):
	_name = 'damage.cause'

	name = fields.Char()

class FleetTrailor(models.Model):
	_name = 'fleet.trailor'

	name = fields.Char()