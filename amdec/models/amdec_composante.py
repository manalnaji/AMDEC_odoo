from odoo import _, api, fields, models


class AmdecComposante(models.Model):
    _name = "amdec.composante"
    _description = "amdec_composante"

    name = fields.Char()

    is_seuil_superior = fields.Boolean()

    seuil = fields.Float()

    valeur = fields.Float()
