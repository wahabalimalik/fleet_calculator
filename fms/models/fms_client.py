# -*- coding: utf-8 -*-
from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class ResPartnerExt(models.Model):
	_inherit = 'res.partner'

	rate = fields.Char()
	# client_route_id = fields.Many2one('fleet.vehicle.route.client','client_id')
	# rate = fields.Char()