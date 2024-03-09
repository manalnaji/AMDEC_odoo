from odoo import _, api, fields, models


class AmdecAmdec(models.Model):
    _name = "amdec.amdec"
    _description = "amdec_amdec"

    name = fields.Char()

    amdec_precedent_id = fields.Integer(string="Amdec Precedent")
