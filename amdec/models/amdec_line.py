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

    failure_mode_id = fields.Many2one(
        comodel_name="amdec.panne.type",
        string="Failure Mode",
    )

    historique_action_ids = fields.Many2many(
        comodel_name="amdec.action.historique",
        string="Historique Action",
    )

    is_seuil_superior = fields.Boolean(
        # store=True, compute="_compute_is_seuil_superior"
    )

    rate = fields.Float(
        help=(
            "Combien de fois la composante apparait dans les actions"
            " historiques."
        ),
        # compute="_compute_rate",
        # store=True,
    )

    system_id = fields.Many2one(
        comodel_name="amdec.system",
        string="System",
    )

    # @api.depends("rate")
    # def _compute_is_seuil_superior(self):
    #     for rec in self:
    #         rec.is_seuil_superior = rec.rate > 0.5
    #
    # # @api.depends("res_model", "res_id")
    # def _compute_rate(self):
    #     pass
