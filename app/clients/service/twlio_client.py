from twilio.rest import Client as TwilioClient
from app.config.app_config import settings

class TwilioService:
    def __init__(self):
        self.client = TwilioClient(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

    def send_message(self, to: str, from_: str, body: str):
        message = self.client.messages.create(
            to=to,
            from_=from_,
            body=body
        )
        return message.sid
