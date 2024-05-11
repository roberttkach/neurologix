package src

import (
	"go.mongodb.org/mongo-driver/bson/primitive"
	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/gridfs"
	"google.golang.org/grpc"
	pb "microservice/proto"
)

type processServer struct {
	db          *mongo.Database
	mlAlgorithm MLAlgorithm
}

func (s *processServer) ProcessImage(ctx context.Context, in *pb.ProcessImageRequest) (*pb.ProcessImageResponse, error) {
	bucket, err := gridfs.NewBucket(s.db)
	if err != nil {
		return nil, grpc.Errorf(grpc.Code(err), "не удалось создать GridFS bucket: %v", err)
	}

	id, err := primitive.ObjectIDFromHex(in.ImageId)
	if err != nil {
		return nil, grpc.Errorf(grpc.Code(err), "не удалось преобразовать идентификатор изображения в ObjectID: %v", err)
	}

	downloadStream, err := bucket.OpenDownloadStream(id)
	if err != nil {
		return nil, grpc.Errorf(grpc.Code(err), "не удалось открыть поток для скачивания: %v", err)
	}
	defer downloadStream.Close()

	image := make([]byte, downloadStream.GetFile().Length)
	_, err = downloadStream.Read(image)
	if err != nil {
		return nil, grpc.Errorf(grpc.Code(err), "не удалось прочитать данные из GridFS: %v", err)
	}

	processedImage, err := s.mlAlgorithm.ProcessImage(image) // предполагается, что ProcessImage - это метод вашего алгоритма ML
	if err != nil {
		return nil, grpc.Errorf(grpc.Code(err), "не удалось обработать изображение: %v", err)
	}

	uploadStream, err := bucket.OpenUploadStreamWithID(primitive.NewObjectID(), "processed_image")
	if err != nil {
		return nil, grpc.Errorf(grpc.Code(err), "не удалось открыть поток для загрузки: %v", err)
	}
	defer uploadStream.Close()

	_, err = uploadStream.Write(processedImage)
	if err != nil {
		return nil, grpc.Errorf(grpc.Code(err), "не удалось записать обработанное изображение в GridFS: %v", err)
	}

	return &pb.ProcessImageResponse{ProcessedImageId: uploadStream.FileID.(primitive.ObjectID).Hex()}, nil
}
