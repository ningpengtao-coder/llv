from llv.faceframe import FaceFrame

import json

import gzip

import struct

frames = json.load(open("examples/arkit_61.json"))

output = "examples/arkit_61.gesichter"

with gzip.open(output, "wb") as file:
        file.write(
            struct.pack(">B", FaceFrame.VERSION)
        )  # version of the binary protocol
        file.write(struct.pack(">L", len(frames)))  # how many frames are in the recording?

        for index,frame in zip(range(0,len(frames)),frames):
            faceFrame = FaceFrame.from_default(frame_number=index)
            faceFrame.blendshapes = frame
            # print(faceFrame.to_json())
            file.write(faceFrame.encode())