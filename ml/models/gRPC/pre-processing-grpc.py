import cv2
import numpy as np
import grpc
from concurrent import futures
import base64
import pre_processing_pb2_pb2
import pre_processing_pb2_grpc


class ImageServiceServicer(pre_processing_pb2_grpc .ImageServiceServicer):
    def ProcessImage(self, request, context):
        nparr = np.fromstring(base64.b64decode(request.image), np.uint8)
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        result = cv2.imencode('.jpg', final_cropped)[1].tostring()
        return your_image_pb2.ImageResponse(result=base64.b64encode(result).decode())


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    your_image_pb2_grpc.add_ImageServiceServicer_to_server(ImageServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()