"""
Copyright 2018 Copenhagen Center for Health Technology (CACHET) at the Technical University of Denmark (DTU).

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the ”Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED ”AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

requirements = ['setuptools', 'requests', 'carp', 'pandas', 'urllib3', 'utils', 'numpy', 'argparse',
                'wheel', 'Jinja2', 'Werkzeug', 'matplotlib', 'seaborn', 'pip', 'tqdm', 'twine']

setup(
    name='carp-python-api',
    version='1.0.0',
    packages=['carp'],
    license='CACHET Research Platform',
    description='The [C]openh[A]gen Center for Health Technology [R]esearch [P]latform (CARP) enables researchers to run mobile health (mHealth) studies where data is collected on participant\'s smartphones and wearable devices. Data is securely uploaded and managed in a hosting infrastructure managed by the Technical University of Denmark (DTU).',
    author="Alban Maxhuni, PhD",
    author_email='almax@dtu.dk',
    long_description=long_description,
    long_description_content_type="text/markdown",
    include_package_data=True,
    install_requires=requirements,
    keywords='carp-python-api',
    url='https://cachet.dk',
    project_urls={
        "CARP Client API - Library": "https://github.com/cph-cachet/carp.python-client-api",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
