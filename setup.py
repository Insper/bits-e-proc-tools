from setuptools import setup, find_packages

setup(
    name="bits",
    version="1.0",
    packages=["bits", "bits.util"],
    include_package_data=True,
    install_requires=["click", "pyyaml", "pytest", "tabulate", "myhdl", "wheel"],
    entry_points="""
        [console_scripts]
        bits=bits:cli
    """,
)
