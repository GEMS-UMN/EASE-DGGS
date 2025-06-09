from setuptools import setup, find_packages

setup(
    name="ease-dggs",
    version="0.2.0",
    description='Python utilities for EASE-based discrete global grid systems',
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
         "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: GIS",
        ],
    license="Apache-2.0",
    project_urls={
        "Homepage": "https://github.com/GEMS-UMN/EASE-DGGS",
        "Repository": "https://github.com/GEMS-UMN/EASE-DGGS",
    },
)
