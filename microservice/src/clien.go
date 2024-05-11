package src

import (
	"context"
	"google.golang.org/grpc"
	"log"
	pb "microservice/proto"
	"os"
	"time"
)

func Client() {
	conn, err := grpc.Dial("localhost:50051", grpc.WithInsecure(), grpc.WithBlock())
	if err != nil {
		log.Fatalf("did not connect: %v", err)
	}
	defer conn.Close()
	c := pb.NewImageProcessingServiceClient(conn)

	// Contact the server and print out its response.
	defaultName := "default"
	name := defaultName
	if len(os.Args) > 1 {
		name = os.Args[1]
	}
	ctx, cancel := context.WithTimeout(context.Background(), time.Second)
	defer cancel()
	r, err := c.UploadImage(ctx, &pb.UploadImageRequest{Image: []byte(name)})
	if err != nil {
		log.Fatalf("could not greet: %v", err)
	}
	log.Printf("Greeting: %s", r.GetImageId())
}
