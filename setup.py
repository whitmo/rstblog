from setuptools import setup, find_packages

setup(
    name='rstblog',
    version='1.0',
    author='Armin Ronacher <armin.ronacher@active-4.com>',
    packages=find_packages(),
    description='',
    long_description='',
    include_package_data = True,
    license="MIT License",
    entry_points = {
    'console_scripts': [ 'run-rstblog = rstblog.cli:main',
                         ],
    },
    install_requires=[
        'Babel',
        'PyYAML',
        'blinker',
        'docutils',
        'jinja2',
        'pygments',
        'werkzeug',
        ],
    )
