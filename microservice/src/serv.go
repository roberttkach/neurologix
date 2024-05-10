package src

import (
	"google.golang.org/grpc"
	"log"
	pb "microservice/proto"
	"net"
)

type server struct {
	pb.UnimplementedImageProcessingServiceServer
}

func Service() {
	lis, err := net.Listen("tcp", ":50051")
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}
	s := grpc.NewServer()
	pb.RegisterImageProcessingServiceServer(s, &server{})
	if err := s.Serve(lis); err != nil {
		log.Fatalf("failed to serve: %v", err)
	}
}
