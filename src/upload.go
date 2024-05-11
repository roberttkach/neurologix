package src

import (
	"context"
	pb "microservice/proto"

	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/bson/primitive"
	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/gridfs"
	"go.mongodb.org/mongo-driver/mongo/options"
	"google.golang.org/grpc"
)

type uploadServer struct {
	db *mongo.Database
}

func (s *uploadServer) UploadImage(ctx context.Context, in *pb.UploadImageRequest) (*pb.UploadImageResponse, error) {
	bucket, err := gridfs.NewBucket(s.db)
	if err != nil {
		return nil, grpc.Errorf(grpc.Code(err), "не удалось создать GridFS bucket: %v", err)
	}

	uploadStream, err := bucket.OpenUploadStream("image.jpg", options.GridFSUpload().SetMetadata(bson.D{{"type", "image"}}))
	if err != nil {
		return nil, grpc.Errorf(grpc.Code(err), "не удалось открыть поток для загрузки: %v", err)
	}
	defer uploadStream.Close()

	_, err = uploadStream.Write(in.Image)
	if err != nil {
		return nil, grpc.Errorf(grpc.Code(err), "не удалось записать данные в GridFS: %v", err)
	}

	fileID := uploadStream.FileID.(primitive.ObjectID)
	return &pb.UploadImageResponse{ImageId: fileID.Hex()}, nil
}
