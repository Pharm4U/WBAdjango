import asyncio
from aiosmtpd.controller import Controller

class CustomSMTP:
    async def handle_DATA(self, server, session, envelope):
        print('Message from: {}'.format(envelope.mail_from))
        print('Message for: {}'.format(envelope.rcpt_tos))
        print('Message data:\n{}'.format(envelope.content.decode()))
        return '250 Message accepted for delivery'

if __name__ == "__main__":
    controller = Controller(CustomSMTP(), hostname='localhost', port=1025)
    controller.start()
    print("SMTP server running on localhost:1025")
    try:
        asyncio.get_event_loop().run_forever()
    except KeyboardInterrupt:
        controller.stop()
        print("SMTP server stopped.")
