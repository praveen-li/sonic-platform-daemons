from setuptools import setup

setup(
    name='sonic-xcvrd',
    version='1.0',
    description='Transceiver monitoring daemon for SONiC',
    license='Apache 2.0',
    author='SONiC Team',
    author_email='linuxnetdev@microsoft.com',
    url='https://github.com/Azure/sonic-platform-daemons',
    maintainer='Kebo Liu',
    maintainer_email='kebol@mellanox.com',
    scripts=[
        'scripts/xcvrd',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: No Input/Output (Daemon)',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.7',
        'Topic :: System :: Hardware',
    ],
    keywords='sonic SONiC TRANSCEIVER transceiver daemon XCVRD xcvrd',
)
