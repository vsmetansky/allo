from setuptools import setup

setup(
    name='allo',
    version='0.1',
    install_requires=(
        'Scrapy>=2.0.0',
    ),
    entry_points={
        'console_scripts': (
            'allo=app:run',
        )
    }
)
