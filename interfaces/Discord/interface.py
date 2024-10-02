from abc import ABC, abstractmethod

from Base import Interface, Entity


class DiscordInterfaceStub(Interface, ABC):
    # client: object

    @abstractmethod
    async def transform(self, ds: object) -> Entity:
        pass
