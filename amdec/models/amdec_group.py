from odoo import _, api, fields, models


class AmdecGroup(models.Model):
    _name = "amdec.group"
    _description = "amdec_group"

    name = fields.Char()

    amdec_id = fields.Many2one(
        comodel_name="amdec.amdec",
        string="Amdec",
    )

    severity = fields.Integer()

    amdec_line_ids = fields.One2many(
        comodel_name="amdec.line",
        inverse_name="amdec_group_id",
        string="Lines",
    )
