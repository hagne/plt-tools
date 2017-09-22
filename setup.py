import sys

required_verion = (3,)
if sys.version_info < required_verion:
    raise ValueError('plt-tools needs at least python {}! You are trying to install it under python {}'.format('.'.join(str(i) for i in required_verion), sys.version))

# import ez_setup
# ez_setup.use_setuptools()

from setuptools import setup
# from distutils.core import setup
setup(
    name="plt_tools",
    version="0.1",
    packages=['plt_tools'],
    author="Hagen Telg",
    author_email="hagen@hagnet.net",
    description="Some of my favorite matplotlib recipes cooked up into a package",
    license="MIT",
    keywords="matplotlib",
    url="https://github.com/hagne/plt-tools",
    # install_requires=['numpy','pandas'],
    # extras_require={'plotting': ['matplotlib'],
    #                 'testing': ['scipy']},
    # test_suite='nose.collector',
    # tests_require=['nose'],
)