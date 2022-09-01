import cv2 
import numpy as np
import onnxruntime as rt
import insightface 
from insightface.app import FaceAnalysis 
from insightface.data import get_image as ins_get_image

class facedetect():
    def __init__(self):
        self.app = FaceAnalysis(allowed_modules=['detection','recognition'],providers=['CUDAExecutionProvider']) # enable detection model only
        self.app.prepare(ctx_id=1, det_size=(640, 640))
    # img = ins_get_image('t1')

    def recognition(self, img):
        # img = ins_get_image(img)
        faces = self.app.get(img)
        return faces