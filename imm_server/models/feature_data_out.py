# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from imm_server.models.base_model_ import Model
from imm_server.models.value_vs_freq import ValueVsFreq  # noqa: F401,E501
from imm_server import util


class FeatureDataOut(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, name: str=None, value: int=None, units: str=None, inrange: str=None, importance: int=None, ranges: List[ValueVsFreq]=None):  # noqa: E501
        """FeatureDataOut - a model defined in Swagger

        :param name: The name of this FeatureDataOut.  # noqa: E501
        :type name: str
        :param value: The value of this FeatureDataOut.  # noqa: E501
        :type value: int
        :param units: The units of this FeatureDataOut.  # noqa: E501
        :type units: str
        :param inrange: The inrange of this FeatureDataOut.  # noqa: E501
        :type inrange: str
        :param importance: The importance of this FeatureDataOut.  # noqa: E501
        :type importance: int
        :param ranges: The ranges of this FeatureDataOut.  # noqa: E501
        :type ranges: List[ValueVsFreq]
        """
        self.swagger_types = {
            'name': str,
            'value': int,
            'units': str,
            'inrange': str,
            'importance': int,
            'ranges': List[ValueVsFreq]
        }

        self.attribute_map = {
            'name': 'name',
            'value': 'value',
            'units': 'units',
            'inrange': 'inrange',
            'importance': 'importance',
            'ranges': 'ranges'
        }
        self._name = name
        self._value = value
        self._units = units
        self._inrange = inrange
        self._importance = importance
        self._ranges = ranges

    @classmethod
    def from_dict(cls, dikt) -> 'FeatureDataOut':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The feature_data_out of this FeatureDataOut.  # noqa: E501
        :rtype: FeatureDataOut
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self) -> str:
        """Gets the name of this FeatureDataOut.


        :return: The name of this FeatureDataOut.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this FeatureDataOut.


        :param name: The name of this FeatureDataOut.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def value(self) -> int:
        """Gets the value of this FeatureDataOut.


        :return: The value of this FeatureDataOut.
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value: int):
        """Sets the value of this FeatureDataOut.


        :param value: The value of this FeatureDataOut.
        :type value: int
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def units(self) -> str:
        """Gets the units of this FeatureDataOut.


        :return: The units of this FeatureDataOut.
        :rtype: str
        """
        return self._units

    @units.setter
    def units(self, units: str):
        """Sets the units of this FeatureDataOut.


        :param units: The units of this FeatureDataOut.
        :type units: str
        """
        if units is None:
            raise ValueError("Invalid value for `units`, must not be `None`")  # noqa: E501

        self._units = units

    @property
    def inrange(self) -> str:
        """Gets the inrange of this FeatureDataOut.

        Value with respect to range  # noqa: E501

        :return: The inrange of this FeatureDataOut.
        :rtype: str
        """
        return self._inrange

    @inrange.setter
    def inrange(self, inrange: str):
        """Sets the inrange of this FeatureDataOut.

        Value with respect to range  # noqa: E501

        :param inrange: The inrange of this FeatureDataOut.
        :type inrange: str
        """
        allowed_values = ["low", "normal", "high"]  # noqa: E501
        if inrange not in allowed_values:
            raise ValueError(
                "Invalid value for `inrange` ({0}), must be one of {1}"
                .format(inrange, allowed_values)
            )

        self._inrange = inrange

    @property
    def importance(self) -> int:
        """Gets the importance of this FeatureDataOut.

        Feature importance in algorithm. The lower the more important the value.  # noqa: E501

        :return: The importance of this FeatureDataOut.
        :rtype: int
        """
        return self._importance

    @importance.setter
    def importance(self, importance: int):
        """Sets the importance of this FeatureDataOut.

        Feature importance in algorithm. The lower the more important the value.  # noqa: E501

        :param importance: The importance of this FeatureDataOut.
        :type importance: int
        """
        if importance is None:
            raise ValueError("Invalid value for `importance`, must not be `None`")  # noqa: E501

        self._importance = importance

    @property
    def ranges(self) -> List[ValueVsFreq]:
        """Gets the ranges of this FeatureDataOut.

        Array defining the normal population in the form of a histogram.  # noqa: E501

        :return: The ranges of this FeatureDataOut.
        :rtype: List[ValueVsFreq]
        """
        return self._ranges

    @ranges.setter
    def ranges(self, ranges: List[ValueVsFreq]):
        """Sets the ranges of this FeatureDataOut.

        Array defining the normal population in the form of a histogram.  # noqa: E501

        :param ranges: The ranges of this FeatureDataOut.
        :type ranges: List[ValueVsFreq]
        """
        if ranges is None:
            raise ValueError("Invalid value for `ranges`, must not be `None`")  # noqa: E501

        self._ranges = ranges