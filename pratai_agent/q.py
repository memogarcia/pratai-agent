# -*- coding: utf-8 -*-

"""
pratai_api.q
~~~~~~~~~~~~
This module contains a function that will send a request to the message
pipeline
"""

import zmq


def send(action, payload, request_id):
    context = zmq.Context()
    sender = context.socket(zmq.PUSH)
    sender.bind('tcp://127.0.0.1:5557')
    try:

        message = {
            'action': action,
            'payload': payload,
            'request_id': request_id
        }
        sender.send_json(message)

    except (KeyboardInterrupt, Exception):
        sender.close()

    finally:
        # responses.close()
        context.close()
