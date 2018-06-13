# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)


	

	# cost_line_id = fields.One2many('product.cost','product_cost_id')

	# @api.onchange('cost_line_id')
	# def on_cost_line_id_change(self):
	# 	self.standard_price = sum(rec.expense_amount for rec in self.cost_line_id)
		
# class ProductCost(models.Model):
# 	_name = 'product.cost'
# 	expense_name = fields.Many2one('expense.type','Name')
# 	expense_amount = fields.Float('Amount')
# 	expense_variable_name = fields.Char('Variable Name')
# 	product_cost_id = fields.Many2one('product.template')

# class ExpenseType(models.Model):
# 	_name = 'fleet.expense.type'

# 	name = fields.Char()

# class VehicleExt(models.Model):
	# _inherit = 'fleet.vehicle'
	# fleet_vehicle_id = fields.Many2one('shipment.cost')
	# sale_ids = fields.Many2many('fleet.sale', compute='_compute_sale_ids', string='Expense associated to this sale')
	# sale_count = fields.Integer(string='Sale Orders', compute='_compute_sale_ids')
	# expense_ids = fields.Many2many('fleet.expense', compute='_compute_expense_ids', string='Expense associated to this expense')
	# expense_count = fields.Integer(string='Expense Orders', compute='_compute_expense_ids')
	
	# @api.multi
	# def _compute_sale_ids(self):
	# 	for order in self:
	# 		sale_ids = self.env['fleet.sale'].search([('name','=',order.name)])
	# 		sale_count = self.env['fleet.sale'].search_count([('name','=',order.name)])
			
	# 		order.update({
	# 			'sale_ids': sale_ids,
	# 			'sale_count': sale_count,
	# 		})

	# @api.multi
	# def action_view_sale(self):
	# 	expense = self.mapped('sale_ids')
	# 	action = self.env.ref('fms.fleet_vehicle_sale_action').read()[0]
	# 	action['views'] = [(self.env.ref('fms.fleet_sales').id, 'form')]
	# 	action['res_id'] = expense.ids[0]
	# 	return action


	# @api.multi
	# def _compute_expense_ids(self):
	# 	for order in self:
	# 		expense_ids = self.env['fleet.expense'].search([('name','=',order.name)])
	# 		expense_count = self.env['fleet.expense'].search_count([('name','=',order.name)])
			
	# 		order.update({
	# 			'expense_ids': expense_ids,
	# 			'expense_count': expense_count,
	# 		})

	# @api.multi
	# def action_view_expense(self):
	# 	expense = self.mapped('expense_ids')
	# 	action = self.env.ref('fms.fleet_vehicle_expense_action').read()[0]
	# 	action['views'] = [(self.env.ref('fms.fleet_expenses').id, 'form')]
	# 	action['res_id'] = expense.ids[0]
	# 	return action