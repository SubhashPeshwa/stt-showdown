from ast import operator
import os
from google.cloud import dialogflow
import time
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./env/ssp.json"

class dflow:

    def __init__(self, project_id, session_id, stream_file, language_code):
        self.project_id = project_id
        self.session_id = session_id
        self.stream_file = stream_file
        self.language_code = language_code

        return None

    @staticmethod
    def _request_generator(audio_config, stream_file, session_path):
        query_input = dialogflow.QueryInput(audio_config=audio_config)

        # The first request contains the configuration.
        yield dialogflow.StreamingDetectIntentRequest(
            session=session_path, query_input=query_input
        )

        # Here we are reading small chunks of audio data from a local
        # audio file.  In practice these chunks should come from
        # an audio input device.
        with open(stream_file, "rb") as audio_file:
            while True:
                chunk = audio_file.read(2048)
                if not chunk:
                    break
                # The later requests contains audio data.
                yield dialogflow.StreamingDetectIntentRequest(input_audio=chunk)

    def transcribe_stream(self, ):
        """Returns the result of detect intent with streaming audio as input.
        Using the same `self.session_id` between requests allows continuation
        of the conversation."""

        session_client = dialogflow.SessionsClient()

        # Note: hard coding audio_encoding and sample_rate_hertz for simplicity.
        audio_encoding = dialogflow.AudioEncoding.AUDIO_ENCODING_LINEAR_16
        sample_rate_hertz = 8000

        session_path = session_client.session_path(self.project_id, self.session_id)
        print("Session path: {}\n".format(session_path))

        audio_config = dialogflow.InputAudioConfig(
            audio_encoding=audio_encoding,
            language_code=self.language_code,
            sample_rate_hertz=sample_rate_hertz,
            single_utterance=False,
        )

        starttime = time.time()
        # every 60 seconds, restart stream
        requests = self._request_generator(audio_config, self.stream_file, session_path)
        responses = self.run(requests)
        # responses = session_client.streaming_detect_intent(requests=requests)

        print("=" * 20)
        for response in responses:
            print(
                'Intermediate transcript: "{}".'.format(
                    response.recognition_result.transcript
                )
            )

        # Note: The result from the last response is the final transcript along
        # with the detected content.
        query_result = response.query_result

        print("=" * 20)
        print("Query text: {}".format(query_result.query_text))
        print(
            "Detected intent: {} (confidence: {})\n".format(
                query_result.intent.display_name, query_result.intent_detection_confidence
            )
        )
        print("Fulfillment text: {}\n".format(query_result.fulfillment_text))

        return None

    def run(self, requests):
        session_client = dialogflow.SessionsClient()

        # Note: hard coding audio_encoding and sample_rate_hertz for simplicity.
        audio_encoding = dialogflow.AudioEncoding.AUDIO_ENCODING_LINEAR_16
        sample_rate_hertz = 8000

        session_path = session_client.session_path(self.project_id, self.session_id)
        print("Session path: {}\n".format(session_path))

        audio_config = dialogflow.InputAudioConfig(
            audio_encoding=audio_encoding,
            language_code=self.language_code,
            sample_rate_hertz=sample_rate_hertz,
            single_utterance=False,
        )
        # requests = self._request_generator(audio_config, self.stream_file, session_path)
        responses = session_client.streaming_detect_intent(requests=requests)
        return responses

    def transcribe_file(stream_file):
        return None

    # def transcribe_mic_input(project_id, session_id, language_code):
    #     """Returns the result of detect intent with live microphone audio as input.
    #     Using the same `session_id` between requests allows continuation
    #     of the conversation."""

    #     session_client = dialogflow.SessionsClient()

    #     audio_encoding = dialogflow.enums.AudioEncoding.AUDIO_ENCODING_LINEAR_16
    #     sample_rate_hertz = 8000

    #     session_path = session_client.session_path(project_id, session_id)

    #     def request_generator(audio_config):
    #         query_input = dialogflow.types.QueryInput(audio_config=audio_config)
    #         yield dialogflow.types.StreamingDetectIntentRequest(session=session_path, query_input=query_input, single_utterance=True)

    #         with MicrophoneStream(RATE, CHUNK) as stream:
    #             #while True:
    #             #Temp condition
    #             while dialogflow.types.StreamingRecognitionResult().is_final == False:
    #                 audio_generated = stream.generator()
    #                 #Temp condition
    #                 if not audio_generated:
    #                     break
    #                 yield dialogflow.types.StreamingDetectIntentRequest(input_audio=audio_generated)

    #     audio_config = dialogflow.types.InputAudioConfig(audio_encoding=audio_encoding, language_code=language_code, sample_rate_hertz=sample_rate_hertz)

    #     requests = request_generator(audio_config)
    #     responses = session_client.streaming_detect_intent(requests)

    #     print('=' * 20)
    #     for response in responses:
    #         print('Intermediate transcript: "{}".'.format(response.recognition_result.transcript)).encode('utf-8')

    #     query_result = response.query_result