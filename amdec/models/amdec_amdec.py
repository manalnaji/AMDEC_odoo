import logging
import random

from odoo import _, api, fields, models

_logger = logging.getLogger(__name__)


class AmdecAmdec(models.Model):
    _name = "amdec.amdec"
    _description = "amdec_amdec"

    name = fields.Char()

    amdec_precedent_id = fields.Many2one(
        comodel_name="amdec.amdec",
        string="AMDEC précédent",
    )

    amdec_group_ids = fields.One2many(
        comodel_name="amdec.group",
        inverse_name="amdec_id",
        string="Groups",
    )

    amdec_line_ids = fields.One2many(
        comodel_name="amdec.line",
        inverse_name="amdec_id",
        string="Lines",
    )

    @api.multi
    def action_execute_algo_1(self):
        self.ensure_one()
        _logger.error("Execute algo 1")
        # Exemple
        for amdec_line in self.amdec_line_ids:
            amdec_line.rate = random.random()
            # amdec_line.is_seuil_superior = bool(random.randint(0, 1))
            amdec_line.is_seuil_superior = amdec_line.rate > 0.5

    @api.multi
    def action_execute_algo_2(self):
        self.ensure_one()
        _logger.error("Execute algo 2")

    # @api.multi
    # @api.returns('self', lambda value: value.id)
    # def copy(self, default=None):
    #     self.ensure_one()
    #     default = dict(default or {})
    #     if 'name' not in default:
    #         default['name'] = _("%s (copy)") % (self.name)
    #     return super(AmdecAmdec, self).copy(default=default)
