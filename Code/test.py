
import pixy
from ctypes import *
from pixy import *
from Motors import *

pixy.init () #Pixy Start#
pixy.change_prog ("color_connected_components");

class Blocks (Structure):
  _fields_ = [ ("m_signature", c_uint),
    ("m_x", c_uint),
    ("m_y", c_uint),
    ("m_width", c_uint),
    ("m_height", c_uint),
    ("m_angle", c_uint),
    ("m_index", c_uint),
    ("m_age", c_uint) ]

blocks = BlockArray(100)
frame = 0
xAxis = 0
yAxis = 0
while 1:
  count = pixy.ccc_get_blocks (100, blocks)
  if count > 0:
    for index in range (0, count):
      prevxAxis = xAxis 
      prevyAxis = yAxis
      # Data Test #print '[BLOCK: SIG=%d X=%3d Y=%3d WIDTH=%3d HEIGHT=%3d]' % (blocks[index].m_signature, blocks[index].m_x, blocks[index].m_y, blocks[index].m_width, 
blocks[index].m_height)
      xAxis =  blocks[index].m_x
      yAxis =  blocks[index].m_y
      if blocks[index].m_signature == 1:
        print("Red Detected")
        forward() 
      elif blocks[index].m_signature == 2:
	print("Yellow Detected")
	backwards()
      else:
	still()
### SHOULD drive forward if red, backwards if yellow
