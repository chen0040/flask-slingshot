from setuptools import setup

setup(
    name='flask_slingshot',
    packages=['flask_slingshot'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ],
)