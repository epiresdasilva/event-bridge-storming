# coding: utf-8
import pprint
import re  # noqa: F401

import six
from enum import Enum

class OrderPlaced(object):


    _types = {
        'customer': 'str',
        'total': 'float'
    }

    _attribute_map = {
        'customer': 'customer',
        'total': 'total'
    }

    def __init__(self, customer=None, total=None):  # noqa: E501
        self._customer = None
        self._total = None
        self.discriminator = None
        self.customer = customer
        self.total = total


    @property
    def customer(self):

        return self._customer

    @customer.setter
    def customer(self, customer):


        self._customer = customer


    @property
    def total(self):

        return self._total

    @total.setter
    def total(self, total):


        self._total = total

    def to_dict(self):
        result = {}

        for attr, _ in six.iteritems(self._types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(OrderPlaced, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, OrderPlaced):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

