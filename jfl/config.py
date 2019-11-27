#!/usr/bin/env python3

from typing import Callable
from lindh.jsonobject import Property, PropertySet, register_schema
from lindh.jsondb import Database


class Config:
    def __init__(self, db_factory: Callable[[], Database]):
        self._database = db_factory('config')
        self.setup_indexes()

    def setup_indexes(self):
        def by_key(obj):
            return obj.get('key'), obj

        self._database.define('by_key', by_key)

    def __getitem__(self, key: str) -> 'ConfigEntry':
        asdict = next(self._database.view('by_key', startkey=key, limit=1), None)
        if asdict is None:
            return None
        entry = ConfigEntry.FromDict(asdict['value'])
        return entry

    def __setitem__(self, key: str, value):
        existing = self[key]
        entry = ConfigEntry(key=key, value=value)
        asdict = entry.to_dict()

        if existing is not None:
            entry.id = existing.id
            entry.revision = existing.revision

        self._database.save(entry.to_dict())


class ConfigEntry(PropertySet):
    id: str = Property(name='_id')
    revision: str = Property(name='_rev')
    key: str = Property('key')
    value = Property(wrap=True)


class ResolutionConfigValue(PropertySet):
    proxy_size: int = Property(default=1280)
    thumb_size: int = Property(default=320)


register_schema(ResolutionConfigValue)


class ServerConfigValue(PropertySet):
    port: int = Property(default=8888)
    host: str = Property(default='127.0.0.1')


register_schema(ServerConfigValue)


class MediaConfigValue(PropertySet):
    mount_path: str = Property()


register_schema(MediaConfigValue)
