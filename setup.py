from setuptools import setup, find_packages

setup(
    name='sdat',
    version='0.1.5',
    url='https://github.com/Chipeyown/SPLiT-seq-Data-Analysis_Toolkit',
    description='A toolkit for analysing SPLiT-seq data',
    author='Chipeyown',
    author_email='chipeyown@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3'

    ],

    keywords='SPLiT-seq',

    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'sdat=sdat:pipeline',
        ],
    },
)
