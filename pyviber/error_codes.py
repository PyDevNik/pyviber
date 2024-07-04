from enum import Enum

class InvalidUrlError(Exception):
    def __str__(self):
        return "Error INVALID_URL (1): The webhook URL is not valid"

class InvalidAuthTokenError(Exception):
    def __str__(self):
        return "Error INVALID_AUTH_TOKEN (2): The authentication token is not valid"

class BadDataError(Exception):
    def __str__(self):
        return "Error BAD_DATA (3): There is an error in the request itself (missing comma, brackets, etc.)"

class MissingDataError(Exception):
    def __str__(self):
        return "Error MISSING_DATA (4): Some mandatory data is missing"

class ReceiverNotRegisteredError(Exception):
    def __str__(self):
        return "Error RECEIVER_NOT_REGISTERED (5): The receiver is not registered to Viber"

class ReceiverNotSubscribedError(Exception):
    def __str__(self):
        return "Error RECEIVER_NOT_SUBSCRIBED (6): The receiver is not subscribed to the account"

class PublicAccountBlockedError(Exception):
    def __str__(self):
        return "Error PUBLIC_ACCOUNT_BLOCKED (7): The account is blocked"

class PublicAccountNotFoundError(Exception):
    def __str__(self):
        return "Error PUBLIC_ACCOUNT_NOT_FOUND (8): The account associated with the token is not an account."

class PublicAccountSuspendedError(Exception):
    def __str__(self):
        return "Error PUBLIC_ACCOUNT_SUSPENDED (9): The account is suspended"

class WebhookNotSetError(Exception):
    def __str__(self):
        return "Error WEBHOOK_NOT_SET (10): No webhook was set for the account"

class ReceiverNoSuitableDeviceError(Exception):
    def __str__(self):
        return "Error RECEIVER_NO_SUITABLE_DEVICE (11): The receiver is using a device or a Viber version that don’t support accounts"

class TooManyRequestsError(Exception):
    def __str__(self):
        return "Error TOO_MANY_REQUESTS (12): Rate control breach"

class ApiVersionNotSupportedError(Exception):
    def __str__(self):
        return "Error API_VERSION_NOT_SUPPORTED (13): Maximum supported account version by all user’s devices is less than the minApiVersion in the message"

class IncompatibleWithVersionError(Exception):
    def __str__(self):
        return "Error INCOMPATIBLE_WITH_VERSION (14): minApiVersion is not compatible to the message fields"

class PublicAccountNotAuthorizedError(Exception):
    def __str__(self):
        return "Error PUBLIC_ACCOUNT_NOT_AUTHORIZED (15): The account is not authorized"

class InchatReplyMessageNotAllowedError(Exception):
    def __str__(self):
        return "Error INCHAT_REPLY_MESSAGE_NOT_ALLOWED (16): Inline message not allowed"

class PublicAccountIsNotInlineError(Exception):
    def __str__(self):
        return "Error PUBLIC_ACCOUNT_IS_NOT_INLINE (17): The account is not inline"

class NoPublicChatError(Exception):
    def __str__(self):
        return "Error NO_PUBLIC_CHAT (18): Failed to post to public account. The bot is missing a Public Chat interface"

class CannotSendBroadcastError(Exception):
    def __str__(self):
        return "Error CANNOT_SEND_BROADCAST (19): Cannot send broadcast message"

class BroadcastNotAllowedError(Exception):
    def __str__(self):
        return "Error BROADCAST_NOT_ALLOWED (20): Attempt to send broadcast message from the bot"

class UnsupportedCountryError(Exception):
    def __str__(self):
        return "Error UNSUPPORTED_COUNTRY (21): The message sent is not supported in the destination country"

class PaymentUnsupportedError(Exception):
    def __str__(self):
        return "Error PAYMENT_UNSUPPORTED (22): The bot does not support payment messages"

class FreeMessagesExceededError(Exception):
    def __str__(self):
        return "Error FREE_MESSAGES_EXCEEDED (23): The bot has reached the monthly threshold"

class NoBalanceError(Exception):
    def __str__(self):
        return "Error NO_BALANCE (24): No balance for a billable bot"

class GeneralError(Exception):
    def __str__(self):
        return f"Error GENERAL_ERROR: General error"

class ErrorCode(Enum):
    """
    Error Codes Enum
    """
    InvalidUrlError = 1
    InvalidAuthTokenError = 2
    BadDataError = 3
    MissingDataError = 4
    ReceiverNotRegisteredError = 5
    ReceiverNotSubscribedError = 6
    PublicAccountBlockedError = 7
    PublicAccountNotFoundError = 8
    PublicAccountSuspendedError = 9
    WebhookNotSetError = 10
    ReceiverNoSuitableDeviceError = 11
    TooManyRequestsError = 12
    ApiVersionNotSupportedError = 13
    IncompatibleWithVersionError = 14
    PublicAccountNotAuthorizedError = 15
    InchatReplyMessageNotAllowedError = 16
    PublicAccountIsNotInlineError = 17
    NoPublicChatError = 18
    CannotSendBroadcastError = 19
    BroadcastNotAllowedError = 20
    UnsupportedCountryError = 21
    PaymentUnsupportedError = 22
    FreeMessagesExceededError = 23
    NoBalanceError = 24
    GeneralError = 25
