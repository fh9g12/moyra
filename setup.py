from setuptools import find_packages, setup
setup(
    name='moyra',
    packages=find_packages(include=['moyra']),
    version='0.1.2',
    description='Generate Multi-body Symbolic and Numeric Equations of Motion',
    long_description = open('README.md').read(),
    long_description_content_type="text/markdown",
    author='Fintan Healy',
    author_email = 'fintan.healy@bristol.ac.uk',
    url='https://https://github.com/fh9g12/moyra',
    license='MIT',
    install_requires=['sympy','numpy','scipy'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)

