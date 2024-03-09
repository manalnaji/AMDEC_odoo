from odoo import _, api, fields, models


class AmdecAmdec(models.Model):
    _name = "amdec.amdec"
    _description = "amdec_amdec"

    name = fields.Char()

    amdec_precedent_id = fields.Many2one(
        comodel_name="amdec.amdec",
        string="AMDEC précédent",
    )

    amdec_group_ids = fields.One2many(
        comodel_name="amdec.group",
        inverse_name="amdec_id",
        string="Groups",
    )

    amdec_line_ids = fields.One2many(
        comodel_name="amdec.line",
        inverse_name="amdec_id",
        string="Lines",
    )
