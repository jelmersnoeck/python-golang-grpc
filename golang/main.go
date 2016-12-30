package main

import (
	"fmt"
	"log"
	"net"
	"os"

	"golang/protos"

	"golang.org/x/net/context"
	"google.golang.org/grpc"
	"google.golang.org/grpc/reflection"
)

type srv struct{}

func (s *srv) Fetch(ctx context.Context, in *protos.Request) (*protos.Response, error) {
	fmt.Println("Receiving request")

	return &protos.Response{Message: "Hello " + in.Name}, nil
}

func main() {
	fmt.Println("Starting server")

	port := os.Getenv("PORT")
	lis, err := net.Listen("tcp", port)
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}

	s := grpc.NewServer()
	protos.RegisterGreeterServer(s, &srv{})
	log.Printf("listening on port: %v\n", port)

	// Register reflection service on gRPC server.
	reflection.Register(s)
	if err := s.Serve(lis); err != nil {
		log.Fatalf("failed to serve: %v", err)
	}
}
