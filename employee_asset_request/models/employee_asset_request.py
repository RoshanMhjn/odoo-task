from odoo import fields, models


class EmployeeAssetRequest(models.Model):
    _name = 'employee.asset.request'
    _description = 'Employee Asset Request'
    _order = 'request_date desc'

    name = fields.Char(
        string='Request',
        required=True,
    )

    employee_id = fields.Many2one(
        'hr.employee',
        string='Employee',
        required=True,
    )

    asset_type = fields.Selection(
        [
            ('laptop', 'Laptop'),
            ('monitor', 'Monitor'),
            ('phone', 'Phone'),
            ('keyboard', 'Keyboard'),
            ('mouse', 'Mouse'),
            ('other', 'Other'),
        ],
        string='Asset Type',
        required=True,
    )

    reason = fields.Text(
        string='Reason',
        required=True,
    )

    request_date = fields.Date(
        string='Request Date',
        default=fields.Date.today,
        required=True,
    )

    state = fields.Selection(
        [
            ('draft', 'Draft'),
            ('submitted', 'Submitted'),
            ('approved', 'Approved'),
            ('rejected', 'Rejected'),
        ],
        string='Status',
        default='draft',
        required=True,
    )

    def action_submit(self):
        for request in self:
            request.state = 'submitted'

    def action_approve(self):
        for request in self:
            request.state = 'approved'

    def action_reject(self):
        for request in self:
            request.state = 'rejected'

    def action_reset_to_draft(self):
        for request in self:
            request.state = 'draft'