# Copyright (c) 2017 StackHPC Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.


import logging

from cliff.lister import Lister

from os_capacity import utils


class FlavorList(Lister):
    """List all the flavors."""

    log = logging.getLogger(__name__)

    def take_action(self, parsed_args):
        flavors = utils.get_flavors(self.app)
        return (('UUID', 'Name', 'VCPUs', 'RAM MB', 'DISK GB'), flavors)


class ListResourcesAll(Lister):
    """List all resource providers, with their resources and servers."""

    def take_action(self, parsed_args):
        inventories = utils.get_providers_with_resources_and_servers(self.app)
        return (('Provider Name', 'Resources', 'Severs'), inventories)


class ListResourcesGroups(Lister):
    """Lists counts of resource providers with similar inventories."""

    def take_action(self, parsed_args):
        groups = utils.group_providers_by_type_with_capacity(self.app)
        return (
            ('Resource Class Groups', 'Total', 'Used', 'Free', 'Flavors'),
            groups)


class ListUsagesAll(Lister):
    """List all current resource usages."""

    def take_action(self, parsed_args):
        allocations = utils.get_allocations_with_server_info(self.app)
        return (
            ('Provider Name', 'Server UUID', 'Resources',
             'Flavor', 'Days', 'Project', 'User'), allocations)
