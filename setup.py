import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="corona-propella",  # Replace with your own username
    version="0.0.1",
    install_requires=[
        "requests",
        "argparse",
    ],
    entry_points={
        'console_scripts': [
            'vails=vails:main',
        ],
    },
    author="kb",
    author_email="okod129@gmail.com",
    description="Hardware on rails with python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kb129/vails/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
