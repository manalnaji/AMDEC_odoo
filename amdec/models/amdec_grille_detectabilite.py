from odoo import _, api, fields, models


class AmdecGrilleDetectabilite(models.Model):
    _name = "amdec.grille.detectabilite"
    _description = "amdec_grille_detectabilite"

    name = fields.Char()

    active = fields.Boolean()

    sequence = fields.Integer()

    value = fields.Integer()

    period_id = fields.Many2one(
        comodel_name="amdec.period",
        string="Période",
    )
