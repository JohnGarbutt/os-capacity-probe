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

import unittest

from os_capacity import utils


class TestUtils(unittest.TestCase):

    def test_get_capacity(self):
        result = utils.get_capacity()
        self.assertEqual(1, len(result))
        self.assertEqual(2, len(result[0]))
        self.assertEqual("foo", result[0]["flavor"])
        self.assertEqual(1, result[0]["count"])