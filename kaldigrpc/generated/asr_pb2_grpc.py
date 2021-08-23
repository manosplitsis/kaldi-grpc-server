# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import asr_pb2 as asr__pb2


class ILSPASRStub(object):
    """
    The ASR service provides two mechanisms for converting speech to text.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Recognize = channel.unary_unary(
                '/ilsp.spmd.asr.ILSPASR/Recognize',
                request_serializer=asr__pb2.RecognizeRequest.SerializeToString,
                response_deserializer=asr__pb2.RecognizeResponse.FromString,
                )
        self.StreamingRecognize = channel.stream_stream(
                '/ilsp.spmd.asr.ILSPASR/StreamingRecognize',
                request_serializer=asr__pb2.StreamingRecognizeRequest.SerializeToString,
                response_deserializer=asr__pb2.StreamingRecognizeResponse.FromString,
                )


class ILSPASRServicer(object):
    """
    The ASR service provides two mechanisms for converting speech to text.
    """

    def Recognize(self, request, context):
        """Recognize expects a RecognizeRequest and returns a RecognizeResponse. This
        request will block until the audio is uploaded, processed, and a transcript
        is returned.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamingRecognize(self, request_iterator, context):
        """StreamingRecognize is a non-blocking API call that allows audio data to be
        fed to the server in chunks as it becomes available. Depending on the
        configuration in the StreamingRecognizeRequest, intermediate results can be
        sent back to the client. Recognition ends when the stream is closed by the
        client.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ILSPASRServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Recognize': grpc.unary_unary_rpc_method_handler(
                    servicer.Recognize,
                    request_deserializer=asr__pb2.RecognizeRequest.FromString,
                    response_serializer=asr__pb2.RecognizeResponse.SerializeToString,
            ),
            'StreamingRecognize': grpc.stream_stream_rpc_method_handler(
                    servicer.StreamingRecognize,
                    request_deserializer=asr__pb2.StreamingRecognizeRequest.FromString,
                    response_serializer=asr__pb2.StreamingRecognizeResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ilsp.spmd.asr.ILSPASR', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ILSPASR(object):
    """
    The ASR service provides two mechanisms for converting speech to text.
    """

    @staticmethod
    def Recognize(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ilsp.spmd.asr.ILSPASR/Recognize',
            asr__pb2.RecognizeRequest.SerializeToString,
            asr__pb2.RecognizeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StreamingRecognize(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/ilsp.spmd.asr.ILSPASR/StreamingRecognize',
            asr__pb2.StreamingRecognizeRequest.SerializeToString,
            asr__pb2.StreamingRecognizeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
