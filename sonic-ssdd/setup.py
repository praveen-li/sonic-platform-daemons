from setuptools import setup

setup(
    name='sonic-ssdd',
    version='1.0',
    description='SSD control daemon for SONiC',
    license='Apache 2.0',
    author='SONiC Team',
    author_email='pmao@linkedin.com',
    url='https://github.com/Azure/sonic-platform-daemons',
    maintainer='Ping Mao',
    maintainer_email='pmao@linkedin.com',
    scripts=[
        'scripts/ssdd',
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
    keywords='sonic SONiC SSD daemon',
)
