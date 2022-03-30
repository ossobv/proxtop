#!/usr/bin/env python
from distutils.core import setup

with open('README.rst') as file:
    long_description = file.read()


setup(
    name='proxtop',
    version='0.3.2',
    scripts=['proxtop'],
    data_files=[('share/doc/proxtop', ['LICENSE.txt', 'README.rst'])],
    description='Proxmox resource monitor',
    long_description=long_description,
    author='Walter Doekes, OSSO B.V.',
    author_email='wjdoekes+proxtop@osso.nl',
    url='https://github.com/ossobv/proxtop',
    license='GPLv3+',
    platforms=['linux'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: System Administrators',
        ('License :: OSI Approved :: GNU General Public License v3 '
         'or later (GPLv3+)'),
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: System :: Clustering',
        'Topic :: System :: Monitoring',
    ],
    install_requires=[
        'proxmoxer>=0.1.7',
        'requests>=2.2.0',
    ],
)

# vim: set ts=8 sw=4 sts=4 et ai tw=79:
