try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='tinymenu',
    version='0.1.0',
    description='Simplifies creation of command-line menus',
    long_description=open('README.md').read(),
    keywords='menu command commandline cli crossplatform xplatform',
    author='QiuDev',
    author_email='qiudev@protonmail.com',
    maintainer='QiuDev',
    url='https://github.com/QiuDev/tinymenu',
    license='MIT',
    python_requires='>=2.6',
    packages=['tinymenu'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Terminals',
    ]
)
