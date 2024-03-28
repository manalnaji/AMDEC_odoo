from odoo import _, api, fields, models


class AmdecGrilleSeverite(models.Model):
    _name = "amdec.grille.severite"
    _description = "amdec_grille_severite"

    name = fields.Char()

    active = fields.Boolean()

    sequence = fields.Integer()

    value = fields.Integer()

    period_id = fields.Many2one(
        comodel_name="amdec.period",
        string="Période",
    )
