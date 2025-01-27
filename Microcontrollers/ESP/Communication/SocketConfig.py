


class SocketConfig:
    def __init__(self):
        self.REQUEST_SIZE = 1  # Request size in byte
        self.PAYLOAD_SIZE = 44  # Payload size in byte
        self.CAMERA_SIZE = 9216  # Camera pic size in byte
        self.TOTAL_SIZE = self.REQUEST_SIZE + self.PAYLOAD_SIZE + self.CAMERA_SIZE

        # Request types
        self.REQ_ACTION = 0
        self.REQ_WEIGHTS = 1
        self.REQ_STATES = 2
        self.REQ_START_WEIGHTS = 3
        self.REQ_LAST_CHUNK = 4
        self.REQ_WAITING_FOR_COMMAND = 1

        # Request Dictionary
        self.commands = {
            0: "stop",
            1: "line_following",
            2: "send_image",
            3: "wait_for_weights",
            4: "use_network",
            5: "no_new_command",
            6: "request_states"
        }


        # States
        self.SEND_IMAGE = 1

        self.WEIGHTS_CHUNKS = 1024  # size of weight chunks

        self.payload_sizes = [28, 16, 9216, 9216]

        self.HOST = '192.168.131.153'  # Standard loopback interface address (localhost)
        self.PORT = 3333  # Port to listen on (non-privileged ports are > 1023)
