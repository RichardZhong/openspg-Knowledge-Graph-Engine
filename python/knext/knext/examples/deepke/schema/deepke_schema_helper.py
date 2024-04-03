# -*- coding: utf-8 -*-
# Copyright 2023 OpenSPG Authors
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except
# in compliance with the License. You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License
# is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied.

# ATTENTION!
# This file is generated by Schema automatically, it will be refreshed after schema has been committed
# PLEASE DO NOT MODIFY THIS FILE!!!
#

from knext.schema.model.schema_helper import (
    SPGTypeHelper,
    PropertyHelper,
    RelationHelper,
)


class DeepKE:
    class BodyPart(SPGTypeHelper):

        description = PropertyHelper("description")
        name = PropertyHelper("name")
        stdId = PropertyHelper("stdId")
        alias = PropertyHelper("alias")
        id = PropertyHelper("id")

    class Disease(SPGTypeHelper):
        class abnormal(RelationHelper):
            shape = PropertyHelper("shape")
            range = PropertyHelper("range")
            color = PropertyHelper("color")

        description = PropertyHelper("description")
        applicableDrug = PropertyHelper("applicableDrug")
        name = PropertyHelper("name")
        commonSymptom = PropertyHelper("commonSymptom")
        complication = PropertyHelper("complication")
        id = PropertyHelper("id")
        department = PropertyHelper("department")
        diseaseSite = PropertyHelper("diseaseSite")

        abnormal = abnormal("abnormal")

    class Drug(SPGTypeHelper):

        description = PropertyHelper("description")
        id = PropertyHelper("id")
        name = PropertyHelper("name")

    class HospitalDepartment(SPGTypeHelper):

        description = PropertyHelper("description")
        name = PropertyHelper("name")
        stdId = PropertyHelper("stdId")
        alias = PropertyHelper("alias")
        id = PropertyHelper("id")

    class Indicator(SPGTypeHelper):

        description = PropertyHelper("description")
        id = PropertyHelper("id")
        name = PropertyHelper("name")

    class Symptom(SPGTypeHelper):

        description = PropertyHelper("description")
        id = PropertyHelper("id")
        name = PropertyHelper("name")

    BodyPart = BodyPart("DeepKE.BodyPart")
    Disease = Disease("DeepKE.Disease")
    Drug = Drug("DeepKE.Drug")
    HospitalDepartment = HospitalDepartment("DeepKE.HospitalDepartment")
    Indicator = Indicator("DeepKE.Indicator")
    Symptom = Symptom("DeepKE.Symptom")

    pass