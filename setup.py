from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='1',
    description='Sorts files and removes empty folders',
    url='https://github.com/An82git/clean_folder.git',
    author='An82git',
    license='MIT',
    packages=find_namespace_packages(),
    install_requires=['shutil', 'pathlib', 'sys', 're'],
    entry_points={'console_scripts': ['clean-folder = clean-folder.clean:main']}
    )