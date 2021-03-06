"""CPython extension for the Hyperscan regular expression engine."""
from __future__ import absolute_import

import io
import subprocess

import setuptools
import setuptools.extension


__all__ = ('setup',)


def readme():
    try:
        with io.open('README.rst') as fp:
            return fp.read()
    except IOError:
        return ''


def setup():
    ext = setuptools.extension.Extension(
        'hyperscan',
        ['src/hyperscanmodule.c'],
        define_macros=[

        ],
        libraries=['hs'],
        extra_compile_args=[
            subprocess.check_output([
                'pkg-config', '--cflags', 'libhs']).decode('utf-8'),
        ],
    )
    setup_requirements = ['six', 'setuptools>=17.1', 'setuptools_scm']
    setuptools.setup(
        author='David Gidwani',
        author_email='david.gidwani@gmail.com',
        classifiers=[
            'Development Status :: 2 - Pre-Alpha',
            'Topic :: Software Development :: Libraries',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'Topic :: Utilities',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: Implementation :: CPython',
            'Environment :: Console',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Operating System :: POSIX :: Linux',
            'Operating System :: Unix',
            'Operating System :: MacOS',
            'Operating System :: Microsoft :: Windows',
        ],
        description=__doc__,
        ext_modules=[ext],
        license='MIT',
        long_description=readme(),
        name='hyperscan',
        setup_requires=setup_requirements,
        url='https://github.com/darvid/python-hyperscan',
        use_scm_version=True,
        zip_safe=False,
    )


if __name__ == '__main__':
    setup()
