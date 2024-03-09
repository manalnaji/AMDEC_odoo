from odoo import _, api, fields, models


class AmdecReparationType(models.Model):
    _name = "amdec.reparation.type"
    _description = "amdec_reparation_type"

    name = fields.Char()
