# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License GPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo.tests.common import TransactionCase
from psycopg2 import IntegrityError


class TestMedicalDrugForm(TransactionCase):

    def setUp(self):
        super(TestMedicalDrugForm, self).setUp()
        self.drug_form_bar = self.env.ref('medical_medicament.BAR')
        self.drug_form_capsule = self.env.ref('medical_medicament.CAP')

    def test_code_unique(self):
        """ Validate drug form unique code sql constraint """
        with self.assertRaises(IntegrityError):
            self.drug_form_bar.code = self.drug_form_capsule.code
