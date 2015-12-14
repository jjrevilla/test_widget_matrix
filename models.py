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
    
    def default_get(self, cr, uid, fields, context=None):
        defaults = super(Project,self).default_get(cr, uid, fields, context=None)
        defaults.update({'name':'Prueba'})
        return defaults


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

    def default_get(self, cr, uid, fields, context=None):
        defaults = super(Manager,self).default_get(cr, uid, fields, context=None)
        
        employee_obj = self.pool.get('test.matrix.employee')
        employee_ids_list =  employee_obj.search(cr, uid, [], context=context)
        employee_names_list = [rec.name for rec in employee_obj.browse(
            cr, uid, employee_ids_list, context=context)]
        
        project_obj = self.pool.get('test.matrix.project')
        project_ids_list =  project_obj.search(cr, uid, [], context=context)
        project_names_list = [rec.name for rec in project_obj.browse(
            cr, uid, project_ids_list, context=context)]        
        
        defaults['task_id'] = [
            (0, 0, {
                'employee_id': e,
                'project_id': p,
                'planned_hours': h
            })
            for e, p, h in zip([employee_names_list],[project_names_list],[12,13,14,15])
        ]        

        defaults['task_id'] = [(0, 0, {'project_id': [u'Prueba 1', u'Employee 1', u'Prueba 3'], 'employee_id': [u'Employee 1', u'Project 2', u'Employee 3'], 'planned_hours': 12}),
                               (0, 0, {'project_id': [u'Prueba 11', u'Employee 2', u'Prueba 3'], 'employee_id': [u'Employee 1', u'Employee 4', u'Employee 33'], 'planned_hours': 22}),
                               (0, 0, {'project_id': [u'Prueba 21', u'Employee 3', u'Prueba 3'], 'employee_id': [u'Employee 1', u'Employee 5', u'Employee 33'], 'planned_hours': 21})
        ]

        return defaults




        
