"""
# Copyright (C) 2007 Rob King (rob@e-mu.org)
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
# For questions regarding this module contact
# Rob King <rob@e-mu.org> or visit http://www.e-mu.org
#
"""

import sys
import Live

errorLog = open("stderr.txt", "w")
errorLog.write("starting stderr log")
stdoutLog = open("stdout.txt", "w")
errorLog.write("starting stdout log")

sys.stderr = errorLog
sys.stdout = stdoutLog

pythonInstallDir = 'C:\\Python22'
sys.path.append(pythonInstallDir)

defaultPythonPaths = ['\\DLLs', '\\lib', '\\lib\\lib-tk', '\\lib\\site-packages', '\\lib\\site-packages\\win32', '\\lib\\plat-win']
for dir in defaultPythonPaths:
    path = pythonInstallDir + dir
    if path not in sys.path:
        sys.path.append(path)

from LiveTelnet import LiveTelnet

def create_instance(c_instance):
    return LiveTelnet(c_instance)
