# -*- coding: utf-8 -*-
###########################################################################
# Copyright (c), The AiiDA team. All rights reserved.                     #
# This file is part of the AiiDA code.                                    #
#                                                                         #
# The code is hosted on GitHub at https://github.com/aiidateam/aiida-core #
# For further information on the license, see the LICENSE.txt file        #
# For further information please visit http://www.aiida.net               #
###########################################################################
"""Backend group module"""

import abc

from . import backends

__all__ = ('BackendLog', 'BackendLogCollection')


class BackendLog(backends.BackendEntity):
    """
    Backend Log interface
    """

    @abc.abstractproperty
    def uuid(self):
        """
        Get the UUID of the log entry

        :return: The entry's UUID
        :rtype: uuid.UUID
        """

    @abc.abstractproperty
    def time(self):
        """
        Get the time corresponding to the entry

        :return: The entry timestamp
        :rtype: :class:`!datetime.datetime`
        """

    @abc.abstractproperty
    def loggername(self):
        """
        The name of the logger that created this entry

        :return: The entry loggername
        :rtype: basestring
        """

    @abc.abstractproperty
    def levelname(self):
        """
        The name of the log level

        :return: The entry log level name
        :rtype: basestring
        """

    @abc.abstractproperty
    def dbnode_id(self):
        """
        Get the id of the object that created the log entry

        :return: The id of the object that created the log entry
        :rtype: int
        """

    @abc.abstractproperty
    def message(self):
        """
        Get the message corresponding to the entry

        :return: The entry message
        :rtype: basestring
        """

    @abc.abstractproperty
    def metadata(self):
        """
        Get the metadata corresponding to the entry

        :return: The entry metadata
        :rtype: dict
        """


class BackendLogCollection(backends.BackendCollection[BackendLog]):
    """The collection of Log entries."""

    ENTITY_CLASS = BackendLog

    @abc.abstractmethod
    def delete(self, log_id):
        """
        Remove a Log entry from the collection with the given id

        :param log_id: id of the Log to delete
        :type log_id: int

        :raises TypeError: if ``log_id`` is not an `int`
        :raises `~aiida.common.exceptions.NotExistent`: if Log with ID ``log_id`` is not found
        """

    @abc.abstractmethod
    def delete_all(self):
        """
        Delete all Log entries.

        :raises `~aiida.common.exceptions.IntegrityError`: if all Logs could not be deleted
        """

    @abc.abstractmethod
    def delete_many(self, filters):
        """
        Delete Logs based on ``filters``

        :param filters: similar to QueryBuilder filter
        :type filters: dict

        :return: (former) ``PK`` s of deleted Logs
        :rtype: list

        :raises TypeError: if ``filters`` is not a `dict`
        :raises `~aiida.common.exceptions.ValidationError`: if ``filters`` is empty
        """
