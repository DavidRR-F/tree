from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Tree command for python'
LONG_DESCRIPTION = 'Tree command for windows plebs'

setup(
    name="tree",
    version=VERSION,
    author="David Rose-Franklin",
    author_email="david.rosefranklin96@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['click'],
    keywords=['create', 'command'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Automation",
        "Programming Language :: Python :: 3+",
        "Operating System :: Microsoft :: Windows",
    ],
    entry_points={
        'console_scripts': [
            'tree=tree.cli:display_tree',
        ],
    },
)
