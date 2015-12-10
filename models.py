# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Employee(models.Model):
    _name = 'test.matrix.employee'
    _rec_name = 'name'
    name = fields.Char(string='First Name', size=10)
    

class Project(models.Model):
    _name = 'test.matrix.project'
    _rec_name = 'name'
    name = fields.Char(string='Name of Project', size=15)


class TasK(models.Model):
    _name = 'test.matrix.task'
    employee_id = fields.Many2one('test.matrix.employee', string='Employee')
    project_id = fields.Many2one('test.matrix.project', string='Project')
    planned_hours = fields.Integer(string='Hours Assigned')
    manager_id = fields.Many2one('test.matrix.manager', string='Manager')    

class Manager(models.Model):
    _name = 'test.matrix.manager'
    task_id = fields.One2many('test.matrix.task', 'manager_id', string='Tasks')
    date_begin = fields.Date(string='From')
    date_end = fields.Date(string='To')
    
    
