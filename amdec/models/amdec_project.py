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
        comodel_name="amdec.period",
        string="Périodes",
    )

    grille_occurence_ids = fields.Many2many(
        comodel_name="amdec.grille.occurence",
        string="Grilles occurence",
    )

    grille_detectabilite_ids = fields.Many2many(
        comodel_name="amdec.grille.detectabilite",
        string="Grilles détectabilite",
    )

    grille_severite_ids = fields.Many2many(
        comodel_name="amdec.grille.severite",
        string="Grilles Sévérité",
    )

    general_amdec_seuil_rpn = fields.Integer()
