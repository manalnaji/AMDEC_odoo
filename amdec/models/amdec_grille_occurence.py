from odoo import _, api, fields, models


class AmdecGrilleOccurence(models.Model):
    _name = "amdec.grille.occurence"
    _description = "amdec_grille_occurence"

    name = fields.Char()

    active = fields.Boolean()

    max_value = fields.Integer()

    min_value = fields.Integer()

    sequence = fields.Integer()
