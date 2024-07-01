from odoo import models, fields, api


class TaskTodo(models.Model):
    _name = 'task1.todo'
    _description = 'task1'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Task Name', tracking=1, required=1)
    partner_id = fields.Many2one('res.partner', string='Assign To', tracking=1)
    date = fields.Date(string='Due Date', tracking=1)
    description = fields.Text(string='Description')
    state = fields.Selection([('new', 'New'), ('in_progress', 'In Progress'), ('completed', 'Completed'), ('closed', 'Closed')],
                             default='new', tracking=1)
    estimated_time = fields.Float()
    line_ids = fields.One2many('task1.timesheet', 'task_id')
    total_lines_time = fields.Float(compute="_compute_total_time", store=True)
    active = fields.Boolean("Active", default=True)
    is_late = fields.Boolean()

    def set_task_new(self):
        for rec in self:
            rec.state = 'new'

    def set_task_in_progress(self):
        for rec in self:
            rec.state = 'in_progress'

    def set_task_completed(self):
        for rec in self:
            rec.state = 'completed'

    def action_closed(self):
        for rec in self:
            rec.state='closed'

    def check_due_date(self):
        task_ids = self.search([])
        for rec in task_ids:
            if rec.date and rec.state in ('new', 'in_progress') and rec.date < fields.Date.today():
                rec.is_late = True

    @api.depends('line_ids.duration')
    def _compute_total_time(self):
        for record in self:
            record.total_lines_time = sum(line.duration for line in record.line_ids)


class Timesheet(models.Model):
    _name = 'task1.timesheet'
    _description = 'Timesheet'

    name = fields.Char(string='Line Title')
    description = fields.Char(string='Description')
    date = fields.Date(string='Line Date')
    duration = fields.Float(string='Line Duration')
    task_id = fields.Many2one('task1.todo')