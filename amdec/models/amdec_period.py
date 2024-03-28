from odoo import _, api, fields, models


class AmdecPeriod(models.Model):
    _name = "amdec.period"
    _description = "amdec_period"

    name = fields.Char()

    date_debut = fields.Date()

    date_fin = fields.Date()
