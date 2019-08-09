from setuptools import setup
from setuptools import find_packages

# PACKAGE NAME AND VERSION
_name = "xml-sort"
_version = "0.1.0"

_description = ""

if __name__ == "__main__":
    setup(
        name=_name,
        version=_version,
        description=_description,
        author='Florian Schaeffeler',
        author_email='florian.schaeffeler@gmail.com',
        entry_points={
            'console_scripts': [
                'xml-sort = xml_sort.__main__:main',
            ]
        },
        packages=find_packages('src'),
        package_dir={'': 'src'},
        # include_package_dara=True, # use MANIFEST.in during install
        package_data={
            # If any package contains *.txt or *.rst files, include them:
            '': ['**/*.*'], },
        install_requires=['lxml'],
        extras_require={
            ':sys_platform == "win32"': [],
            ':"linux" in sys_platform': []
        },
        tests_require=['pytest'],
        cmdclass={}
    )