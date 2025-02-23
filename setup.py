import setuptools
import re


def get_long_description():
    with open('README.md') as f:
        raw_readme = f.read()
    base_repo = 'https://github.com/equinor/seismic-zfp/tree/'
    with open('.git/refs/heads/master') as f:
        commit = f.read().rstrip()
    substituted_readme = re.sub('\\]\\((?!https)', '](' + base_repo + commit + '/', raw_readme)
    return substituted_readme


setuptools.setup(name='seismic-zfp',
                 author='equinor',
                 description='Compress and decompress seismic data',
                 long_description=get_long_description(),
                 long_description_content_type='text/markdown',
                 url='https://github.com/equinor/seismic-zfp',
                 license='LGPL-3.0',

                 use_scm_version=True,
                 install_requires=['numpy>=1.16', 'numpy>=1.20; python_version>="3.9.0"',
                                   'segyio', 'zfpy', 'psutil', 'click'],
                 extras_require={
                     'zgy': ['zgy2sgz>=0.1.3']
                 },
                 setup_requires=['setuptools', 'setuptools_scm'],
                 entry_points="""
                     [console_scripts]
                     seismic-zfp=seismic_zfp.cli:cli
                 """,
                 packages=['seismic_zfp']
                 )
