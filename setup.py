from setuptools import setup

setup(
    name='rstblog',
    version='1.0',
    author='Armin Ronacher <armin.ronacher@active-4.com>',
    packages=['rstblog', 'rstblog.modules'],
    description='',
    long_description='',
    license='BSD License',
    entry_points = {
        'console_scripts': ['run-rstblog = rstblog.cli:main'],
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
