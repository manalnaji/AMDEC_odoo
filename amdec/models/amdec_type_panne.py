from odoo import _, api, fields, models


class AmdecTypePanne(models.Model):
    _name = "amdec.type_panne"
    _description = "amdec_type_panne"

    name = fields.Char()
