from odoo import _, api, fields, models


class AmdecProject(models.Model):
    _name = "amdec.project"
    _description = "amdec_project"

    name = fields.Char()
