"""
Created on Dec 18, 2014

@author: tcanham, reder

"""
from __future__ import print_function
from __future__ import absolute_import
import struct
from .type_exceptions import TypeMismatchException
from .type_exceptions import TypeRangeException
from . import type_base


@type_base.serialize
@type_base.deserialize
class I32Type(type_base.BaseType):
    """
    Representation of the I32 type
    """

    def __init__(self, val=None):
        """
        Constructor
        """
        self.__val = val
        if val == None:
            return

        self._check_val(val)

    def _check_val(self, val):
        if not type(val) == type(int()):
            raise TypeMismatchException(type(int()), type(val))

        # check range
        if (val < -pow(2, 31)) or (val > pow(2, 31) - 1):
            raise TypeRangeException(val)

    @property
    def val(self):
        return self.__val

    @val.setter
    def val(self, val):
        self._check_val(val)
        self.__val = val

    def serialize(self):
        """
        Utilize serialize decorator here...
        """
        return self._serialize(">i")

    def deserialize(self, data, offset):
        """
        Utilize deserialized decorator here...
        """
        self._deserialize(">i", data, offset)

    def getSize(self):
        return struct.calcsize(">i")

    def __repr__(self):
        return "I32"
