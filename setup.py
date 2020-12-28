from setuptools import setup, find_packages

setup(
    name             = 'mtodo',
    version          = '0.0.1',
    author           = 'neelabalan',
    author_email     = 'neelabalan.n@gmail.com',
    packages         = find_packages(),
    url              = 'https://github.com/neelabalan/mtodo',
    license          = 'LICENSE',
    description      = 'A Terminal app for parsing todo and adding it to Microsoft To-Do.',
    install_requires = [
        'toml',
        'requests',
        'msal',
    ],
    include_package_data = True,
    entry_points         = ''' 
        [console_scripts] 
        mtodo = mtodo.mtodo:main
    ''',
    python_requires = '>=3.6',
    # setup_requires  = [ 'wheel' ]
)
