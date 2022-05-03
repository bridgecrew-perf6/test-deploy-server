from setuptools import find_packages, setup

long_description = 'Test Deploy Server'

setup(
    name='test-deploy-server',
    version='0.1.10',
    setup_cfg=True,
    python_requires='>=3.8',
    packages=find_packages(where='.'),
    include_package_data=True,
    long_description=long_description,
    long_description_content_type='text/markdown',
    setup_requires=['setuptools>=54.0.0'],
    test_suite='tests',
    zip_safe=True
)