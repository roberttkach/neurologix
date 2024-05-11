package src

import (
	"context"
	"go.mongodb.org/mongo-driver/bson/primitive"
	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/gridfs"
	"google.golang.org/grpc"
	pb "microservice/proto"
)

type downloadServer struct {
	db *mongo.Database
}

func (s *downloadServer) DownloadImage(ctx context.Context, in *pb.DownloadImageRequest) (*pb.DownloadImageResponse, error) {
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

	return &pb.DownloadImageResponse{Image: image}, nil
}
