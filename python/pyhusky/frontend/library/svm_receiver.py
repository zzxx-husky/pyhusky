# Copyright 2016 Husky Team
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

class SVMReceiver(object):
    def __init__(self):
        pass

    @staticmethod
    def register(receiver_map):
        receiver_map["SVMModel#SVM_train_py"] = SVMReceiver.train_receiver
        receiver_map["SVMModel#SVM_test_py"] = SVMReceiver.test_receiver

    @staticmethod
    def train_receiver(reply):
        res = []
        # eat dummy int64 represents the string length
        dummy = reply.load_int64()
        n_params = reply.load_int32()
        for _ in xrange(n_params):
            param_v = reply.load_double()
            res.append(param_v)
        return res

    @staticmethod
    def test_receiver(reply):
        reply.load_int64()
        return reply.load_double()
