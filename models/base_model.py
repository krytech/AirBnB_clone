#!/usr/bin/python3
""" Base model. """
from datetime import datetime
from string import digits
import uuid
from . import storage


class BaseModel:
    """ All common attributes/methods for derived classes. """

    def __init__(self, *args, **kwargs):
        """ Initialize model. """
        if len(kwargs):
            for k, v in kwargs.items():
                # Do not set "__class__"; done automatically
                if k == "__class__":
                    continue
                setattr(self, k, v)
            # Convert ISO format time strings to datetime objects
            self.created_at = self.from_iso_format(self.created_at)
            self.updated_at = self.from_iso_format(self.updated_at)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """ Return human readable string representation of model. """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__
        )

    def save(self):
        """ Update "updated_at" time. """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ Return json serializable dictionary representation of model. """
        d = {k: v for k, v in self.__dict__.items()}
        d.update(
            {
                "__class__": self.__class__.__name__,
                "created_at": self.created_at.isoformat(),
                "updated_at": self.updated_at.isoformat()
            }
        )
        return d

    @staticmethod
    def from_iso_format(t):
        """ Convert ISO format datetime string into datetime object. """
        args = [t[0:4], t[5:7], t[8:10], t[11:13], t[14:16], t[17:19], t[20:]]
        args = [int(t) for t in args]
        return datetime(*args)
