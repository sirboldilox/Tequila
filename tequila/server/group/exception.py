"""
Tequila: a command-line Minecraft server manager written in python

Copyright (C) 2014 Snaipe

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
from ...exception import TequilaException


class ServerGroupException(TequilaException):
    def __init__(self, message, group, **kwargs):
        super().__init__(message, name=group.name, **kwargs)
        self.server = group


class ServerGroupDoesNotExistException(ServerGroupException):
    def __init__(self, group):
        super().__init__('Server group $name does not exist', group)


class ServerGroupAlreadyExistsException(ServerGroupException):
    def __init__(self, group):
        super().__init__('Server group $name already exists', group)