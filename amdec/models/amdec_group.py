from odoo import _, api, fields, models


class AmdecGroup(models.Model):
    _name = "amdec.group"
    _description = "amdec_group"

    name = fields.Char()

    amdec_id = fields.Many2one(
        comodel_name="_unknown",
        string="Amdec",
    )

    severity = fields.Integer()
