#!/usr/bin/env python3
#
# Copyright 2021 howto author
#
# SPDX-License-Identifier: GPL-3.0-or-later
#
#

from newsched import gr, gr_unittest, blocks
from newsched import howto

class test_copy(gr_unittest.TestCase):

    def setUp(self):
        self.tb = gr.flowgraph()

    def tearDown(self):
        self.tb = None

    def test_000(self):
        tb = self.tb
        src_data = [float(x) for x in range(0, 100)]
        expected_result = src_data.copy()

        src = blocks.vector_source_f(src_data)
        op = howto.copy(gr.sizeof_float)
        dst = blocks.vector_sink_f()

        tb.connect(src, op)
        tb.connect(op, dst)
        tb.run()
        dst_data = dst.data()
        self.assertEqual(expected_result, dst_data)



if __name__ == '__main__':
    gr_unittest.run(test_copy)
