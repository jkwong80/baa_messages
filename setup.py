from setuptools import setup, find_packages
import sys
import baa_messages
version = baa_messages.__version__

setup(name='baa_messages',
      version=version,
      description='SDK For working with Berkeley Applied Analytics cloud tools',
      author='Berkeley Applied Analytics',
      author_email='',
      url='https://github.com/berkeleyapplied/baa_messages',
      packages=find_packages(exclude='test'),
      package_data={'': ["*.so"]},
      license='MIT License',
      test_suite='test',
      install_requires=[
          'thrift',
          'pre-commit',
          'AWSIoTPythonSDK',
          'Enum',
          'pypubsub'
      ],
      tests_require=[
	'thrift',
        'AWSIoTPythonSDK',
        'Enum',
        'pypubsub',
        'mock'
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
