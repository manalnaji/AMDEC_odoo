from odoo import _, api, fields, models


class AmdecProject(models.Model):
    _name = "amdec.project"
    _description = "amdec_project"

    name = fields.Char()

    amdec_ids = fields.One2many(
        comodel_name="amdec.amdec",
        inverse_name="amdec_project_id",
        string="AMDEC",
    )

    period_ids = fields.Many2many(
        comodel_name="amdec.period", string="Périodes", help="COMPUTE"
    )

    grille_occurence_ids = fields.Many2many(
        comodel_name="amdec.grille.occurence",
        string="Grilles occurence",
        help="COMPUTE",
    )

    grille_detectabilite_ids = fields.Many2many(
        comodel_name="amdec.grille.detectabilite",
        string="Grilles détectabilite",
        help="COMPUTE",
    )

    grille_severite_ids = fields.Many2many(
        comodel_name="amdec.grille.severite",
        string="Grilles Sévérité",
        help="COMPUTE",
    )

    general_amdec_seuil_rpn = fields.Integer(
        help="Default value from configuration."
    )
