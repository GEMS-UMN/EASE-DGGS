from setuptools import setup, find_packages

from setuptools import setup, find_packages

setup(
    name="ease-dggs",
    version="0.2.0",
    description='EASE-DGGS Library Code and Tools',
    url='https://github.com/GEMS-UMN/EASE-DGGS',
    author='GEMS Geospatial Developers',
    author_email='gemssupport@umn.edu',
    packages=find_packages(),  # No need for `where="src"` here
    include_package_data=True,
    install_requires=[
        'pytest',
        'pyproj >= 3.2.1',
        'geopandas >= 0.10.0',
        'numpy >= 1.21.2',
        'pandas >= 1.3.3',
        'shapely >= 1.7.1',
        'rasterio >= 1.2',
        ],
    python_requires=">=3.9",
    classifiers=[
        'Programming Language :: Python :: 3.9',
        ],
    license="Apache-2.0",
)

