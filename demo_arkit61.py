from llv.faceframe import FaceFrame

import json

import gzip

import struct

# frames = json.load(open("examples/arkit_61.json"))

# output = "examples/arkit_61.gesichter"

# with gzip.open(output, "wb") as file:
#         file.write(
#             struct.pack(">B", FaceFrame.VERSION)
#         )  # version of the binary protocol
#         file.write(struct.pack(">L", len(frames)))  # how many frames are in the recording?

#         for index,frame in zip(range(0,len(frames)),frames):
#             faceFrame = FaceFrame.from_default(frame_number=index)
#             faceFrame.blendshapes = frame
#             # print(faceFrame.to_json())
#             file.write(faceFrame.encode())

input = "F:/arkit61.gesichter.gz"
input1 = "examples/arkit_61.gesichter"

from llv.cli import read_frames

fps = 60

for frame_package in read_frames(input, loop=True):
    frame_data, frame_index, frame_count, version = frame_package
    if 0 == frame_index:
        print(
            f"Start sending {frame_count} frames of version {version} @{fps}fps ..."
        )

    frame = FaceFrame.from_raw(frame_data, len(frame_data))
    break

for frame_package in read_frames(input1, loop=True):
    frame_data, frame_index, frame_count, version = frame_package
    if 0 == frame_index:
        print(
            f"Start sending {frame_count} frames of version {version} @{fps}fps ..."
        )

    frame1 = FaceFrame.from_raw(frame_data, len(frame_data))
    break

print(frame.blendshapes == frame1.blendshapes)
    # bytes_sent = buchse.send(frame.data, frame.size)
    # # print(frame_data)
    # # bytes_sent = buchse.send(frame_data, len(frame_data))
    # if bytes_sent != len(frame_data):
    #     raise Exception(
    #         f"Error sending full frame! ({bytes_sent}/{len(frame_data)})"
    #     )

    # try:
    #     time.sleep(sleep_time)
    # except KeyboardInterrupt:
    #     print("Stopping playback ...")
    #     break