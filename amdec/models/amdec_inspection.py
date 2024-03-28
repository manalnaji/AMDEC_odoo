from odoo import _, api, fields, models


class AmdecInspection(models.Model):
    _name = "amdec.inspection"
    _description = "amdec_inspection"

    name = fields.Char()

    date_action = fields.Date()

    defaillance_id = fields.Many2one(
        comodel_name="amdec.defaillance",
        string="Défaillance",
    )

    responsable_action_id = fields.Many2one(
        comodel_name="res.partner", string="Responsable"
    )

    frequence = fields.Integer(help="Par défaut, devrait être 0 ou 1")
