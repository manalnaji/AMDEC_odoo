from odoo import _, api, fields, models


class AmdecPanneType(models.Model):
    _name = "amdec.panne.type"
    _description = "amdec_panne_type"

    name = fields.Char()
