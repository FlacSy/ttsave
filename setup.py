from setuptools import setup, find_packages
# from Cython.Build import cythonize
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
    package_data={
        "ttsave": ["*.pyd", "utils/*.pyd", "js/xbogus-js.min.js"],
    },
    entry_points={
        'console_scripts': [
            'ttsave=ttsave_cli:cli',
        ],
    },
    # ext_modules=cythonize(
    #     [
    #         "ttsave/lib.py",
    #         "ttsave/utils/xbogus.py"
    #     ],
    #     compiler_directives={"language_level": "3"},
    #     annotate=True,
    # ),
    zip_safe=False,
    packages=find_packages(),
)
