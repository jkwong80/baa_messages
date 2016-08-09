from setuptools import setup
import sys

version = '0.0.1'

setup(name='baa_messages',
      version=version,
      description='Thrift Message formats',
      author='Berkely Applied Analytics',
      author_email='',
      url='https://github.com/berkeleyapplied/baa_messages',
      packages=['baa_messages', 'test'],
      license='MIT License',
      test_suite='test',
      install_requires=[
          'thrift',
          'pre-commit',
          'AWSIoTPythonSDK',
          'Enum'
      ],
      tests_require=[
	'thrift',
        'AWSIoTPythonSDK',
        'Enum'
      ],
      platforms=['any'],
      classifiers=['Development Status :: 1 - Alpha',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: MIT License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 2.7',
                   'Topic :: Software Development',
                   'Topic :: Software Development :: Libraries',
                   'Topic :: Software Development :: Libraries :: Python Modules']
    )
