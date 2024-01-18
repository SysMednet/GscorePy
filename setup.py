from setuptools import setup

requirements = [
    'numpy',
    'pandas',
    'scipy',
    'statsmodels',
    'matplotlib',
    'seaborn',
]

setup(
    name='GscorePy',
    version='0.0.1',
    description="GscorePy is a python implementation of Gscore.",
    author="SysMednet",
    author_email='medsb.net@gmail.com',
    url='https://github.com/SysMednet/GscorePy',
    install_requires=requirements,
    packages=[
        'GscorePy',
    ],
    package_dir={'GscorePy': 'Gscore'},
    package_data={'GscorePy':['Database/*/*/*','Database/*/*','Database/*']},
    license="MIT license",
    zip_safe=True,
    keywords='Gscore',
    classifiers=[
        'Programming Language :: Python :: 3.9.13',
    ],
)
