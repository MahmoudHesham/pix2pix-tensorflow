'''
Created on Dec 2, 2017

@author: flyn
'''
import os
_dir = os.path.dirname(__file__)

model = os.path.join(_dir, "facades_sandbox/export")
output_file = os.path.join(_dir, "facades_sandbox/output_dir/output_inference.png")
tmp_file = os.path.join(_dir, "facades_sandbox/input_dir/image.png")

buttons_dict = {"Wall": (13,61,251),
                "Door": (165,0,0),
                "Window": (0,117,255),
                "W.Sill": (104,248,152),
                "W.Head": (29,255,221),
                "Shutter": (238,237,40),
                "Balcony": (184,255,56),
                "Trim": (255,146,4),
                "Cornice": (255,68,1),
                "Column": (246,0,1),
                "Entrance": (0,201,255)}