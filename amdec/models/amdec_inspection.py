from odoo import _, api, fields, models


class AmdecInspection(models.Model):
    _name = "amdec.inspection"
    _description = "amdec_inspection"

    name = fields.Char()

    date_action = fields.Date()

    frequence = fields.Integer()
