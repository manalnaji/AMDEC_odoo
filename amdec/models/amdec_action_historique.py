from odoo import _, api, fields, models


class AmdecActionHistorique(models.Model):
    _name = "amdec.action.historique"
    _description = "amdec_action_historique"

    name = fields.Char()

    action_corrige_panne = fields.Boolean()

    action_realise = fields.Boolean()

    action_reparation = fields.Char()

    composante_id = fields.Many2one(
        comodel_name="amdec.composante",
        string="Composante",
    )

    system_id = fields.Many2one(
        comodel_name="amdec.system",
        string="System",
    )

    type_panne_id = fields.Many2one(
        comodel_name="amdec.type_panne",
        string="Type Panne",
    )
