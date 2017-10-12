import unittest
from paddle.v2.framework.graph import Variable, g_program
import paddle.v2.framework.core as core
import numpy as np


class TestVariable(unittest.TestCase):
    def test_np_dtype_convert(self):
        DT = core.DataType
        convert = Variable._convert_np_dtype_to_dtype_
        self.assertEqual(DT.FP32, convert(np.float32))
        self.assertEqual(DT.FP16, convert("float16"))
        self.assertEqual(DT.FP64, convert("float64"))
        self.assertEqual(DT.INT32, convert("int32"))
        self.assertEqual(DT.INT16, convert("int16"))
        self.assertEqual(DT.INT64, convert("int64"))
        self.assertEqual(DT.BOOL, convert("bool"))
        self.assertRaises(ValueError, lambda: convert("int8"))

    def test_var(self):
        b = g_program.current_block()
        w = b.create_var(
            dtype="float64", shape=[784, 100], lod_level=0, name="fc.w")
        self.assertEqual(core.DataType.FP64, w.data_type)
        self.assertEqual((784, 100), w.shape)
        self.assertEqual("fc.w", w.name)
        self.assertEqual(0, w.lod_level)

        w = b.create_var(name='fc.w')
        self.assertEqual(core.DataType.FP64, w.data_type)
        self.assertEqual((784, 100), w.shape)
        self.assertEqual("fc.w", w.name)
        self.assertEqual(0, w.lod_level)

        self.assertRaises(ValueError,
                          lambda: b.create_var(name="fc.w", shape=(24, 100)))


if __name__ == '__main__':
    unittest.main()
