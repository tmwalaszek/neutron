#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from neutron_lib.api import extensions as api_extensions


# The name of the extension.
NAME = "Security group rules update"

# The alias of the extension.
ALIAS = "security-groups-rules-update"

# The description of the extension.
DESCRIPTION = ("Allow updating a security group rule in place, instead of "
               "having to delete it and create a replacement.")

# The list of required extensions.
REQUIRED_EXTENSIONS = ['security-group']

# The list of optional extensions.
OPTIONAL_EXTENSIONS = None

# The date the extension was introduced.
UPDATED_TIMESTAMP = "2026-08-24T10:00:00-00:00"


class Security_groups_rules_update(api_extensions.ExtensionDescriptor):
    """Extension class supporting updates of security group rules.

    This extension does not add any attribute of its own; it flips
    allow_put on the existing security group rule attributes that may be
    changed. It exists so that the capability is discoverable through
    GET /v2.0/extensions, rather than clients having to issue a PUT and
    interpret the failure.
    """

    @classmethod
    def get_name(cls):
        return NAME

    @classmethod
    def get_alias(cls):
        return ALIAS

    @classmethod
    def get_description(cls):
        return DESCRIPTION

    @classmethod
    def get_updated(cls):
        return UPDATED_TIMESTAMP

    def get_required_extensions(self):
        return REQUIRED_EXTENSIONS or []

    def get_optional_extensions(self):
        return OPTIONAL_EXTENSIONS or []

    def get_extended_resources(self, version):
        return {}
