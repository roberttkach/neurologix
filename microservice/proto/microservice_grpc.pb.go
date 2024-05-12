// Code generated by protoc-gen-go-grpc. DO NOT EDIT.
// versions:
// - protoc-gen-go-grpc v1.2.0
// - protoc             v3.20.3
// source: microservice.proto

package microservice

import (
	context "context"
	grpc "google.golang.org/grpc"
	codes "google.golang.org/grpc/codes"
	status "google.golang.org/grpc/status"
)

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
// Requires gRPC-Go v1.32.0 or later.
const _ = grpc.SupportPackageIsVersion7

// ImageProcessingServiceClient is the client API for ImageProcessingService service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type ImageProcessingServiceClient interface {
	UploadImage(ctx context.Context, in *UploadImageRequest, opts ...grpc.CallOption) (*UploadImageResponse, error)
	DownloadImage(ctx context.Context, in *DownloadImageRequest, opts ...grpc.CallOption) (*DownloadImageResponse, error)
	ProcessImage(ctx context.Context, in *ProcessImageRequest, opts ...grpc.CallOption) (*ProcessImageResponse, error)
	GetNumbers(ctx context.Context, in *GetNumbersRequest, opts ...grpc.CallOption) (*GetNumbersResponse, error)
	SendMetrics(ctx context.Context, in *SendMetricsRequest, opts ...grpc.CallOption) (*SendMetricsResponse, error)
	LogMetrics(ctx context.Context, in *LogMetricsRequest, opts ...grpc.CallOption) (*LogMetricsResponse, error)
}

type imageProcessingServiceClient struct {
	cc grpc.ClientConnInterface
}

func NewImageProcessingServiceClient(cc grpc.ClientConnInterface) ImageProcessingServiceClient {
	return &imageProcessingServiceClient{cc}
}

func (c *imageProcessingServiceClient) UploadImage(ctx context.Context, in *UploadImageRequest, opts ...grpc.CallOption) (*UploadImageResponse, error) {
	out := new(UploadImageResponse)
	err := c.cc.Invoke(ctx, "/proto.ImageProcessingService/UploadImage", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *imageProcessingServiceClient) DownloadImage(ctx context.Context, in *DownloadImageRequest, opts ...grpc.CallOption) (*DownloadImageResponse, error) {
	out := new(DownloadImageResponse)
	err := c.cc.Invoke(ctx, "/proto.ImageProcessingService/DownloadImage", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *imageProcessingServiceClient) ProcessImage(ctx context.Context, in *ProcessImageRequest, opts ...grpc.CallOption) (*ProcessImageResponse, error) {
	out := new(ProcessImageResponse)
	err := c.cc.Invoke(ctx, "/proto.ImageProcessingService/ProcessImage", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *imageProcessingServiceClient) GetNumbers(ctx context.Context, in *GetNumbersRequest, opts ...grpc.CallOption) (*GetNumbersResponse, error) {
	out := new(GetNumbersResponse)
	err := c.cc.Invoke(ctx, "/proto.ImageProcessingService/GetNumbers", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *imageProcessingServiceClient) SendMetrics(ctx context.Context, in *SendMetricsRequest, opts ...grpc.CallOption) (*SendMetricsResponse, error) {
	out := new(SendMetricsResponse)
	err := c.cc.Invoke(ctx, "/proto.ImageProcessingService/SendMetrics", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *imageProcessingServiceClient) LogMetrics(ctx context.Context, in *LogMetricsRequest, opts ...grpc.CallOption) (*LogMetricsResponse, error) {
	out := new(LogMetricsResponse)
	err := c.cc.Invoke(ctx, "/proto.ImageProcessingService/LogMetrics", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// ImageProcessingServiceServer is the server API for ImageProcessingService service.
// All implementations must embed UnimplementedImageProcessingServiceServer
// for forward compatibility
type ImageProcessingServiceServer interface {
	UploadImage(context.Context, *UploadImageRequest) (*UploadImageResponse, error)
	DownloadImage(context.Context, *DownloadImageRequest) (*DownloadImageResponse, error)
	ProcessImage(context.Context, *ProcessImageRequest) (*ProcessImageResponse, error)
	GetNumbers(context.Context, *GetNumbersRequest) (*GetNumbersResponse, error)
	SendMetrics(context.Context, *SendMetricsRequest) (*SendMetricsResponse, error)
	LogMetrics(context.Context, *LogMetricsRequest) (*LogMetricsResponse, error)
	mustEmbedUnimplementedImageProcessingServiceServer()
}

// UnimplementedImageProcessingServiceServer must be embedded to have forward compatible implementations.
type UnimplementedImageProcessingServiceServer struct {
}

func (UnimplementedImageProcessingServiceServer) UploadImage(context.Context, *UploadImageRequest) (*UploadImageResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method UploadImage not implemented")
}
func (UnimplementedImageProcessingServiceServer) DownloadImage(context.Context, *DownloadImageRequest) (*DownloadImageResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method DownloadImage not implemented")
}
func (UnimplementedImageProcessingServiceServer) ProcessImage(context.Context, *ProcessImageRequest) (*ProcessImageResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method ProcessImage not implemented")
}
func (UnimplementedImageProcessingServiceServer) GetNumbers(context.Context, *GetNumbersRequest) (*GetNumbersResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetNumbers not implemented")
}
func (UnimplementedImageProcessingServiceServer) SendMetrics(context.Context, *SendMetricsRequest) (*SendMetricsResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method SendMetrics not implemented")
}
func (UnimplementedImageProcessingServiceServer) LogMetrics(context.Context, *LogMetricsRequest) (*LogMetricsResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method LogMetrics not implemented")
}
func (UnimplementedImageProcessingServiceServer) mustEmbedUnimplementedImageProcessingServiceServer() {
}

// UnsafeImageProcessingServiceServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to ImageProcessingServiceServer will
// result in compilation errors.
type UnsafeImageProcessingServiceServer interface {
	mustEmbedUnimplementedImageProcessingServiceServer()
}

func RegisterImageProcessingServiceServer(s grpc.ServiceRegistrar, srv ImageProcessingServiceServer) {
	s.RegisterService(&ImageProcessingService_ServiceDesc, srv)
}

func _ImageProcessingService_UploadImage_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(UploadImageRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(ImageProcessingServiceServer).UploadImage(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/proto.ImageProcessingService/UploadImage",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(ImageProcessingServiceServer).UploadImage(ctx, req.(*UploadImageRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _ImageProcessingService_DownloadImage_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(DownloadImageRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(ImageProcessingServiceServer).DownloadImage(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/proto.ImageProcessingService/DownloadImage",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(ImageProcessingServiceServer).DownloadImage(ctx, req.(*DownloadImageRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _ImageProcessingService_ProcessImage_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ProcessImageRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(ImageProcessingServiceServer).ProcessImage(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/proto.ImageProcessingService/ProcessImage",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(ImageProcessingServiceServer).ProcessImage(ctx, req.(*ProcessImageRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _ImageProcessingService_GetNumbers_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(GetNumbersRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(ImageProcessingServiceServer).GetNumbers(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/proto.ImageProcessingService/GetNumbers",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(ImageProcessingServiceServer).GetNumbers(ctx, req.(*GetNumbersRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _ImageProcessingService_SendMetrics_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(SendMetricsRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(ImageProcessingServiceServer).SendMetrics(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/proto.ImageProcessingService/SendMetrics",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(ImageProcessingServiceServer).SendMetrics(ctx, req.(*SendMetricsRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _ImageProcessingService_LogMetrics_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(LogMetricsRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(ImageProcessingServiceServer).LogMetrics(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/proto.ImageProcessingService/LogMetrics",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(ImageProcessingServiceServer).LogMetrics(ctx, req.(*LogMetricsRequest))
	}
	return interceptor(ctx, in, info, handler)
}

// ImageProcessingService_ServiceDesc is the grpc.ServiceDesc for ImageProcessingService service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var ImageProcessingService_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "proto.ImageProcessingService",
	HandlerType: (*ImageProcessingServiceServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "UploadImage",
			Handler:    _ImageProcessingService_UploadImage_Handler,
		},
		{
			MethodName: "DownloadImage",
			Handler:    _ImageProcessingService_DownloadImage_Handler,
		},
		{
			MethodName: "ProcessImage",
			Handler:    _ImageProcessingService_ProcessImage_Handler,
		},
		{
			MethodName: "GetNumbers",
			Handler:    _ImageProcessingService_GetNumbers_Handler,
		},
		{
			MethodName: "SendMetrics",
			Handler:    _ImageProcessingService_SendMetrics_Handler,
		},
		{
			MethodName: "LogMetrics",
			Handler:    _ImageProcessingService_LogMetrics_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "microservice.proto",
}