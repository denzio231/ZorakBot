import setuptools

import versioneer

setuptools.setup(
    name="zorak",
    description="An installable version of the Zorak.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    package_dir={"": "src"},
    include_package_data=True,
    packages=setuptools.find_packages(where="src"),
    entry_points={"console_scripts": ["zorak=__main__:main"]},
    package_data={"": ["*.toml"]},
    install_requires=[
        "py-cord",
        "beautifulsoup4",
        "requests",
        "matplotlib",
        "DateTime",
        "pytz",
        "pistonapi",
        "toml",
        "feedparser",
        "html2text",
        "pymongo",
        "youtube_dl",
    ],
    classifiers=[
        # see https://pypi.org/classifiers/
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3 :: Only",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    extras_require={
        "dev": [
            "cfgv==3.3.1"
            "distlib==0.3.6"
            "filelock==3.9.0"
            "identify==2.5.17"
            "nodeenv==1.7.0"
            "platformdirs==3.0.0"
            "pre-commit==3.0.4"
            "PyYAML==6.0"
            "ruff==0.0.243"
            "virtualenv==20.19.0"
        ],
        # 'test': ['coverage'],
    },
)
