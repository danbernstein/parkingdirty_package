from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='Parking Dirty Object Detection',
    url='https://github.com/danbernstein/parkingdirty_package',
    author='Dan Bernstein',
    author_email='danbernstein94@gmail.com',
    # Needed to actually package something
    #packages=['setup'],
    # Needed for dependencies
    install_requires=['numpy'],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='MIT',
    description='a python function for processing parking dirty data',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)
