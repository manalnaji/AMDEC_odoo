from odoo import _, api, fields, models


class AmdecSystem(models.Model):
    _name = "amdec.system"
    _description = "amdec_system"

    name = fields.Char()
