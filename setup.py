from setuptools import setup, find_packages

setup(
    name='bioplus',
    version='0.0.0',
    packages= find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'openpyxl'
    ],
    entry_points={
      'console_scripts':['f_d=bioplus.db_ena:ena_downloader']
    }
)
