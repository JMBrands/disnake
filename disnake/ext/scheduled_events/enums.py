from enum import Enum
class EventStatus(Enum):
    SCHEDULED = 1
    ACTIVE = 2
    COMPLETED = 3
    CANCELED = 4

class EventPrivacyLevel(Enum):
    GUILD_ONLY = 2

class EventEntityType(Enum):
    STAGE_INSTANCE = 1
    VOICE = 2
    EXTERNAL = 3
