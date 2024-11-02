import jxlpy
import random
from ctypes import *

size = (64, 64)

ImageType = c_short * (size[0] * size[1])
original_image = ImageType()

# fill the image with random 12bit data
for i in range(0, len(original_image)):
	original_image[i] = random.randint(0, 2**12 - 1)

original_data = bytes(original_image)
enc = jxlpy.JXLPyEncoder(quality=100, colorspace='L', size=size, effort=7, use_container=True, bit_depth=12,
	frame_bit_depth=jxlpy.JxlPyBitDepth(jxlpy.JxlPyBitDepthType.FROM_CODESTREAM))
enc.add_frame(original_data)

encoded = enc.get_output()

dec = jxlpy.JXLPyDecoder(encoded, frame_bit_depth=jxlpy.JxlPyBitDepth(jxlpy.JxlPyBitDepthType.FROM_CODESTREAM))
decoded = dec.get_frame()

if decoded == original_data:
	print("Lossless encoding was successful")
else:
	print("Lossless encoding was not successful")