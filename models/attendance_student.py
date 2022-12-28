# -*- coding: utf-8 -*-

from odoo import models, fields

class StudentInfo(models.Model):
    _name = "attendance.student"
    _description = "All informations about is here."

    name = fields.Char("Name",required = True)
    student_id = fields.Char("Student Id",required = True)
    email = fields.Char("Email")
    course = fields.Many2many("attendance.course", string="Student Course")
    year  = fields.Integer("Year")
    semester = fields.Integer("Semester")
    date = fields.Date("Date",default=fields.Datetime.now())
    subject = fields.Many2one("attendance.subject", string = "Subject")
    faculty = fields.Many2one("attendance.faculty" ,string="Faculty")
    department_name = fields.Many2one("attendance.department" ,string="Department")
    state = fields.Selection(selection=[('pending','Pending'),('done','Done')],default="pending")
    active = fields.Boolean(default=True)