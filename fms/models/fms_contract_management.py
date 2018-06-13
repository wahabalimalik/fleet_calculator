# -*- coding: utf-8 -*-
from odoo import api, fields, models


class FleetVehicleContract(models.Model):
    _inherit = 'fleet.vehicle.log.contract'
    _description = "Vehicle Contract"

    # vehicle_id = fields.Many2one('fleet.vehicle','Vehicle', required=True)
    vehicle_number = fields.Char('Vehicle Number', related="vehicle_id.license_plate" )
    trailor_id = fields.Many2one('fleet.trailor','Trailor Number')
    
    sumatra_start_date = fields.Date('Sumatra Start')
    sumatra_expiration_date = fields.Date('Sumatra Expiration')
    kenya_start_date = fields.Date('Kenya Start')
    kenya_expiration_date = fields.Date('Kenya Expiration')

    # date = fields.Date(required=True)
    # employee_id = fields.Many2one( 'hr.employee', string="Driver", domain=[('driver', '=', True)])
    # location = fields.Char()
    # accident_report = fields.Text('Accident Report')
    # damage_cause = fields.Many2many('damage.cause')