# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 CERN.
# Copyright (C) 2019 Northwestern University.
#
# Invenio-RDM-Records is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.

"""Record serializers."""

from ..marshmallow import RecordSchemaV1
from invenio_resources.serializers.record import JSONRercordSerializer

json_v1 = JSONRercordSerializer(RecordSchemaV1)
