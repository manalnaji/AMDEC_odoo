# Copyright 2023 TechnoLibre inc. - Mathieu Benoit
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).


from odoo import api, fields, models

DEFAULT_AMDEC_SEUIL = 0.1


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    # ----------------------------------------------------------
    # Database
    # ----------------------------------------------------------

    default_seuil = fields.Float(
        default=DEFAULT_AMDEC_SEUIL,
        default_model="amdec.composante",
        string="Seuil de composante AMDEC par défaut",
        help="Default seuil for a AMDEC composante.",
    )

    # ----------------------------------------------------------
    # Functions
    # ----------------------------------------------------------

    @api.multi
    def set_values(self):
        res = super(ResConfigSettings, self).set_values()
        param = self.env["ir.config_parameter"].sudo()
        param.set_param("amdec.default_seuil", self.default_seuil)
        return res

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        params = self.env["ir.config_parameter"].sudo()
        res.update(
            default_seuil=float(
                params.get_param("amdec.default_seuil", DEFAULT_AMDEC_SEUIL)
            )
        )
        return res
