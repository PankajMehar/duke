from distutils.core import setup

setup(name='Duke',
    version='1.1.0',
    description='Character-level CNN+LSTM model for text classification',
    packages=['Duke'],
    install_requires=['Faker >= 0.7.7',
        'scikit-learn >= 0.18.1',
        'python-dateutil >= 2.5.3',
        'pandas >= 0.19.2',
        'numpy>=1.13.3',
        'scipy >= 0.19.0',
        'tensorflow >= 1.1.0',
        'gensim>=3.2.0',
        'h5py >= 2.7.0'],
    include_package_data=True,
)