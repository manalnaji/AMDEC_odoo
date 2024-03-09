from odoo import _, api, fields, models


class AmdecLine(models.Model):
    _name = "amdec.line"
    _description = "amdec_line"

    name = fields.Char()

    amdec_group_id = fields.Many2one(
        comodel_name="amdec.group",
        string="Amdec Group",
    )

    amdec_id = fields.Many2one(
        comodel_name="amdec.amdec",
        string="Amdec",
    )

    color = fields.Char()

    failure_mode_id = fields.Many2one(
        comodel_name="amdec.type_panne",
        string="Failure Mode",
    )

    historique_action_ids = fields.Many2many(
        comodel_name="amdec.action.historique",
        string="Historique Action",
    )

    is_seuil_superior = fields.Boolean()

    rate = fields.Float()

    system_id = fields.Many2one(
        comodel_name="amdec.system",
        string="System",
    )
