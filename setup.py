from setuptools import setup

setup(
    name='term_dashboard_backend',
    packages=['term_dashboard_backend'],
    include_package_data=True,
    install_requires=[
        'flask',
        'pymongo',
        'passlib',
    ],
)