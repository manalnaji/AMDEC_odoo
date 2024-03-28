from odoo import _, api, fields, models


class AmdecLine(models.Model):
    _name = "amdec.line"
    _description = "amdec_line"

    name = fields.Char()

    amdec_id = fields.Many2one(
        comodel_name="amdec.amdec",
        string="Amdec",
    )

    defaillance_id = fields.Many2one(
        comodel_name="amdec.defaillance",
        string="Défaillance",
    )

    failure_mode_id = fields.Many2one(
        comodel_name="amdec.panne.type",
        string="Failure Mode",
    )

    historique_action_ids = fields.Many2many(
        comodel_name="amdec.action.historique",
        string="Historique Action",
    )

    effet = fields.Text()

    cause = fields.Text()

    is_seuil_superior = fields.Boolean(store=True, compute="_compute_rpn")

    general_amdec_seuil_rpn = fields.Integer(
        related="amdec_id.amdec_project_id.general_amdec_seuil_rpn"
    )

    inspection_ids = fields.Many2many(
        comodel_name="amdec.inspection",
        string="Inspections",
    )

    occurence = fields.Integer(
        help=(
            "Calcul du nombre de fréquence sur l'ensemble des inspections par"
            " période de temps en appliquant la grille des seuils d'occurences"
            " dynamiques."
        ),
        compute="_compute_occurence",
        store=True,
    )

    detectabilite_id = fields.Many2one(
        comodel_name="amdec.grille.detectabilite"
    )

    severite_id = fields.Many2one(comodel_name="amdec.grille.severite")

    rpn = fields.Integer(store=True, compute="_compute_rpn")

    composante_id = fields.Many2one(
        comodel_name="amdec.composante", string="Composante"
    )

    system_id = fields.Many2one(
        related="composante_id.system_id",
        string="System",
    )

    @api.depends(
        "rpn",
        "occurence",
        "detectabilite_id",
        "severite_id",
        "general_amdec_seuil_rpn",
    )
    def _compute_rpn(self):
        for rec in self:
            if rec.detectabilite_id and rec.severite_id and rec.occurence:
                rec.rpn = (
                    rec.occurence
                    * rec.detectabilite_id.value
                    * rec.severite_id.value
                )
                rec.is_seuil_superior = rec.rpn > rec.general_amdec_seuil_rpn
            else:
                rec.rpn = False

    @api.depends(
        "amdec_id.amdec_project_id.grille_occurence_ids", "inspection_ids"
    )
    def _compute_occurence(self):
        for rec in self:
            rec.occurence = 4
