# The MIT License (MIT)
# Copyright (c) 2014 Microsoft Corporation

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""Internal Helper functions in the Azure Cosmos database service.
"""

import platform
import re
from . import http_constants


def get_user_agent():
    os_name = safe_user_agent_header(platform.system())
    os_version = safe_user_agent_header(platform.release())
    python_version = safe_user_agent_header(platform.python_version())

    user_agent = "{}/{} Python/{} {}/{}".format(
        os_name, os_version, python_version, http_constants.Versions.SDKName, http_constants.Versions.SDKVersion
    )
    return user_agent


def safe_user_agent_header(s):
    if s is None:
        s = "unknown"
    # remove all white spaces
    s = re.sub(r"\s+", "", s)
    if not s:
        s = "unknown"
    return s
