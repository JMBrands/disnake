import datetime
from typing import (
    # TYPE_CHECKING,
    # Any,
    # Callable,
    # Dict,
    # Generic,
    # List,
    # Mapping,
    Optional,
    # Set,
    # TypeVar,
    # Union,
)
import disnake
from enums import (
    EventEntityType,
    EventPrivacyLevel,
    EventStatus,
)

class EventEntityMetadata:
    def __init__(self, location:Optional[str]=None) -> None:
        self.location = location

class ImageData:
    def __init__(self, media_type:str, data:str, base64_extension:bool) -> None:
        self.media_type = media_type
        self.base64_extension = base64_extension
        self.data = data

class ScheduledEvent:
    """
    Represents a scheduled event that can be organised in a guild.
    This class is used to schedule guild evnts using a bot.

    A number of options can be passed to the :Class:`ScheduledEvent`.

    Parameters
    ----------
    name: :class:`str`
        The name of the event
    entity_type: :class:`EventEntityType`
        The type of event: stage, voice or external
    privacy_level: :class:`EventPrivacyLevel`
        The privacy level of th event, currently the only option is 'guild only'
    scheduled_start_time: :class:`datetime.datetime`
        The time at which the event is scheduled to start
    scheduled_end_time: :class:`Optional[datetime.datetime]`
        The time at which the event is scheduled to end, only optional for events with entity_type external, otherwise necessary
    channel_id: :class:`Optional[int]`
        The id of the channel where the event will take place, only optional for events with entity_type external, otherwise necessary
    description: :class:`Optional[str]`
        Description for th event
    entity_metadata: :class:`Optional[EventEntityMetadata]`
        Metadata for the event, just location for external events right now
    image: :class:`Optional[ImageData]`
        ImageData URI for the cover image for the event
    """
    def __init__(self,
                 name:str,
                 entity_type:EventEntityType,
                 privacy_level:EventPrivacyLevel,
                 scheduled_start_time:datetime.datetime,
                 scheduled_end_time:Optional[datetime.datetime]=None,
                 channel_id:Optional[int]=None,
                 description:Optional[str]=None,
                 entity_metadata:Optional[EventEntityMetadata]=None,
                 image:Optional[ImageData]=None,
                 ) -> None:
        self.id: Optional[int] = None
        self.guild_id:Optional[int]=None
        self.creator_id:Optional[int]=None
        self.status:Optional[EventStatus]=None
        self.entity_id:Optional[int]=None
        self.creator:Optional[disnake.User]=None
        self.user_count:Optional[int]=None
        self.channel_id=channel_id
        self.name=name
        self.description=description
        self.scheduled_start_time=scheduled_start_time
        self.privacy_level=privacy_level
        self.entity_type=entity_type
        self.scheduled_end_time=scheduled_end_time
        self.entity_metadata=entity_metadata
        self.image=image
ScheduledEvent("name", EventEntityType.EXTERNAL, EventPrivacyLevel.GUILD_ONLY, datetime.datetime.now())
disnake.Client()