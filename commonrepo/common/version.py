# -*- coding: utf-8 -*-

#
# Copyright 2016 edX PDR Lab, National Central University, Taiwan.
#
#     http://edxpdrlab.ncu.cc/
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Created By: yrchen@ATCity.org
# Maintained By: yrchen@ATCity.org
#

"""
Utilities of version in Common Repository project.
"""

from subprocess import Popen, PIPE

from commonrepo import __version__


def get_git_version2():
    """
    https://github.com/RevSquare/gipsy/blob/master/README.rst
    """
    import subprocess

    def call(cmd):
        return subprocess.Popen(cmd, stdout=subprocess.PIPE, cwd=BASE_DIR).communicate()[0]

    describe = call(['git', 'describe'])
    branch = call(['git', 'rev-parse', '--abbrev-ref', 'HEAD'])
    sha = call(['git', 'rev-parse', '--short', 'HEAD'])
    if branch.strip() == 'master':
        return describe, sha
    return branch, describe

# https://github.com/lambdalisue/django-package-skeleton/edit/master/packageutils/version.py
#
# Author: Douglas Creager <dcreager@dcreager.net>
#
# Calculates the current version number.  If possible, this is the
# output of “git describe”, modified to conform to the versioning
# scheme that setuptools uses.  If “git describe” returns an error
# (most likely because we're in an unpacked copy of a release tarball,
# rather than in a git working copy), then we fall back on reading the
# contents of the RELEASE-VERSION file.
#
# To use this script, simply import it your setup.py file, and use the
# results of get_git_version() as your package version:
#
# from version import *
#
# setup(
#     version=get_git_version(),
#     .
#     .
#     .
# )
#
# This will automatically update the RELEASE-VERSION file, if
# necessary.  Note that the RELEASE-VERSION file should *not* be
# checked into git; please add it to your top-level .gitignore file.
#
# You'll probably want to distribute the RELEASE-VERSION file in your
# sdist tarballs; to do this, just create a MANIFEST.in file that
# contains the following line:
#
#   include RELEASE-VERSION

__all__ = ("get_git_version")


def call_git_describe(abbrev=4):
    try:
        p = Popen(['git', 'describe', '--abbrev=%d' % abbrev],
                  stdout=PIPE, stderr=PIPE)
        p.stderr.close()
        line = p.stdout.readlines()[0]
        return line.strip()

    except:
        return None


def read_release_version():
    try:
        f = open("RELEASE-VERSION", "r")

        try:
            version = f.readlines()[0]
            return version.strip()

        finally:
            f.close()

    except:
        return None


def write_release_version(version):
    f = open("RELEASE-VERSION", "w")
    f.write("%s\n" % version)
    f.close()


def get_git_version(abbrev=4):
    # Read in the version that's currently in RELEASE-VERSION.

    release_version = read_release_version()

    # First try to get the current version using “git describe”.

    version = call_git_describe(abbrev)

    # If that doesn't work, fall back on the value that's in
    # RELEASE-VERSION.

    if version is None:
        version = release_version

    # If we still don't have anything, that's an error.
    #
    # yrchen: In CommonRepo, we still have another __version__ variable
    #         stored in the package.
    #         On production environment, use the variable to avoid raise
    #         the exception
    if version is None:
        version = __version__

    # If the current version is different from what's in the
    # RELEASE-VERSION file, update the file to be current.

    if version != release_version:
        write_release_version(version)

    # Finally, return the current version.
    return version
