#!/usr/bin/python3
""" Define BaseModel. """
from datetime import datetime
import uuid


class BaseModel:
    """ Define all common attributes/methods for derived classes. """

    def __init__(self):
        """ Initialize model. """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ Return human readable string representation of model. """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__
        )

    def save(self):
        """ Update 'updated_at' time. """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ Return json serializable dictionary representation of model. """
        d = {k: v for k, v in self.__dict__.items()}
        d.update(
            {
                "__class__": __class__.__name__,
                "created_at": self.created_at.isoformat(),
                "updated_at": self.updated_at.isoformat()
            }
        )
        return d
