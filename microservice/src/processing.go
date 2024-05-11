package src

import (
	"log"
	pb "microservice/proto"
)

func Process() {
	r2, err := c.ProcessImage(ctx, &pb.ProcessImageRequest{ImageId: r.GetImageId()})
	if err != nil {
		log.Fatalf("Не удалось обработать изображение: %v", err)
	}
	log.Printf("Processed Image ID: %s", r2.GetProcessedImageId())
}
