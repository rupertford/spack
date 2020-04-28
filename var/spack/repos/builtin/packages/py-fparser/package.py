# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyFparser(PythonPackage):
    '''Native Python parser for Fortran 2003 and the majority of Fortran
    2008.

    '''
    homepage = "https://github.com/stfc/fparser"
    url = "https://github.com/stfc/fparser/archive/0.0.10.tar.gz"
    git = "https://github.com/stfc/fparser.git"

    maintainers = ['rupertford', 'arporter']

    version('master', branch='master')
    version('0.0.10', sha256='729a1b4dd215d07a7555625066b4ba48388d5523598a7'
            '5bf225186c738de2b97')
    version('0.0.5', sha256='7668b331b9423d15353d502ab26d1d561acd5247882dab'
            '672f1e45565dabaf08')

    depends_on('py-setuptools', type=('build', 'run'))
    depends_on('py-six', type=('build', 'run'))
