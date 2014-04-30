import logging

import time
import pusherclient


PUSHER_APP_KEY = 'cb65d0a7a72cd94adf1f'
THROTTLE = 0.1


class PusherSub:
    """Wrapper for pusherclient."""

    def __init__(self, callback, *chans):
        self.pusher = pusherclient.Pusher(PUSHER_APP_KEY)
        self._callback = callback
        self._chans = chans


    def _bind(self, channel, event_name):
        def _bind_callback(data):
            channel.bind(event_name, self._event(channel))
        return _bind_callback

    def _subscribe(self, event_name):
        def subscribe_callback(data):
            for channel_name in self._chans:
                channel = self.pusher.subscribe(channel_name)
                channel.bind('pusher_internal:subscription_succeeded',
                             self._bind(channel, event_name))
        return subscribe_callback

    def connect(self):
        self.pusher.connection.bind('pusher:connection_established',
                                    self._subscribe('message'))
        self.pusher.connect()


class CryptsyApp(PusherSub):
    """ """

    def _event(self, channel):
        def _event_callback(message):
            print(channel.name, message)
        return _event_callback



if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    p = CryptsyApp(*['trade.' + str(i) for i in range(200)])
    #p = CryptsyApp("trade.3")
    p.connect()

    while True:
        time.sleep(THROTTLE)