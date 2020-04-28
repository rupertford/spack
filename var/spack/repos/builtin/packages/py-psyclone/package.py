# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
from spack import *


class PyPsyclone(PythonPackage):
    '''Code parser and domain specific compiler for finite
    difference/volume/element weather and climate models. Used in the
    LFRic model at the UK Met Office.

    '''
    homepage = "https://github.com/stfc/PSyclone"
    url = "https://github.com/stfc/PSyclone/archive/1.8.1.tar.gz"
    git = "https://github.com/stfc/PSyclone.git"

    maintainers = ['rupertford', 'arporter', 'sergisiso', 'hiker', 'TeranIvy']

    version('master', branch='master')
    version('1.8.1', sha256='3ed264fe6e25a71e06ab8161f4b6f499d46e4d10dce3d93'
            '0b6ef4f8b380ca2b8')
    version('1.5.1', sha256='643f5b7a62dd3c16bd91955d6bce91cfe6fa268528255248'
            '82d04201643da79c')

    depends_on('py-setuptools', type=('build', 'run'))
    depends_on('py-pyparsing', type=('build', 'run'))
    depends_on('py-six', type=('build', 'run'))
    depends_on('py-enum34', type=('build', 'run'))
    depends_on('py-configparser', type=('build', 'run'))

    # PSyclone versions may require particular versions of fparser
    depends_on('py-fparser@master', type=('build', 'run'), when='@master')
    depends_on('py-fparser@0.0.10', type=('build', 'run'), when='@1.8.1')
    depends_on('py-fparser@0.0.5', type=('build', 'run'), when='@1.5.1')

    def setup_run_environment(self, env):
        '''Set the PSyclone config-file environment variable to point to the
        default config-file provided in the distribution.

        '''
        install_path = os.path.join(
            self.prefix, "share", "psyclone", "psyclone.cfg")
        env.set('PSYCLONE_CONFIG', install_path)
