from setuptools import setup

requirements = [
    'numpy',
    'pandas',
    'scipy',
    'statsmodels',
    'matplotlib',
    'seaborn'
]

package_data_format = {'gscorepy':['Database/**/**/**/*', #graph_files/font-awesome-4.0.3
                                 'Database/**/**/*', #geneset
                                 'Database/**/*' ]}  #graph_code_fragment, graph_files(first layer)

setup(
    name='gscorepy',
    version='0.0.1',
    description="GscorePy is a python implementation of Gscore.",
    author="SysMednet",
    author_email='medsb.net@gmail.com',
    url='https://github.com/SysMednet/GscorePy',
    install_requires=requirements,
    packages=[
        'gscorepy',
    ],
    package_dir={'gscorepy': 'Gscore'},
    package_data=package_data_format,
    license="MIT license",
    zip_safe=True,
    keywords=['Gscore','gscorepy','pathway analysis','enrichment'],
    classifiers=[
        'Programming Language :: Python :: 3.9.13',
    ]
)
