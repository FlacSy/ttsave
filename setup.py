from setuptools import setup
from Cython.Build import cythonize
from ttsave.__version__ import __version__

def readme():
    with open('README.md', 'r', encoding='utf-8') as f:
        return f.read()

def install_requires():
    with open('requirements.txt', 'r', encoding='utf-8') as f:
        return f.readlines()

setup(
    name='ttsave',
    version=__version__,
    description='A simple tool to save TikTok videos',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/FlacSy/ttsave',
    author='FlacSy',
    author_email='flacsy.tw@gmail.com',
    license='Apache',
    py_modules=['ttsave_cli'],
    install_requires=install_requires(),
    entry_points={
        'console_scripts': [
            'ttsave=ttsave_cli:cli',
        ],
    },
    zip_safe=False,
    ext_modules=cythonize(
        [
            "ttsave/lib.py",
            "ttsave/utils/xbogus.py"
        ],
        compiler_directives={"language_level": "3"},
        annotate=False,
    ),
)
