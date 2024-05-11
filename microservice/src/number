package src

import (
	"context"
	"log"
	pb "microservice/proto"
	"time"

	"google.golang.org/grpc"
)

func num() ([]int32, error) {
	conn, err := grpc.Dial("localhost:50051", grpc.WithInsecure(), grpc.WithBlock())
	if err != nil {
		log.Printf("Не удалось подключиться: %v", err)
		return nil, err
	}
	defer conn.Close()
	c := pb.NewImageProcessingServiceClient(conn)

	ctx, cancel := context.WithTimeout(context.Background(), time.Second)
	defer cancel()

	r3, err := c.GetNumbers(ctx, &pb.GetNumbersRequest{ProcessedImageId: "your_processed_image_id"})
	if err != nil {
		log.Printf("Не удалось получить числа: %v", err)
		return nil, err
	}

	return r3.GetNumbers(), nil
}

func NmberOutput() {
	numbers, err := num()
	if err != nil {
		log.Printf("Не удалось получить числа: %v", err)
		// Добавьте здесь вашу логику обработки ошибок
		return
	}
	for _, num := range numbers {
		log.Printf("Number: %v", num)
	}
}
