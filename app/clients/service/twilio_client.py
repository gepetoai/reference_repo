from twilio.rest import Client as TwilioClient
from app.core.config import settings
from app.monitoring.logging import get_logger

logger = get_logger(__name__)

class TwilioService:
    def __init__(self):
        self.client = TwilioClient(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

    def send_message(self, to: str, from_: str, body: str):
        try:
            message = self.client.messages.create(
                to=to,
                from_=from_,
                body=body
            )
            return message.sid
        except Exception as e:
            logger.error(f"Failed to send message to {to}: {str(e)}")
            raise RuntimeError(f"Failed to send message to {to}: {str(e)}")
