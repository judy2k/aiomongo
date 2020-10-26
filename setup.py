from setuptools import setup, find_packages

EXTRAS_REQUIRE = {
    "tests": [
        "pytest",
        "coverage[toml]>=5.0.2",
    ],
}
EXTRAS_REQUIRE["dev"] = EXTRAS_REQUIRE["tests"] + [
    "black",
    "twine",
    "wheel",
    "prospector[with_everything]",
]

setup(
    name="aiomongo",
    description="A fully async, maybe sans-io MongoDB driver.",
    version="0.0.0",
    author="Mark Smith",
    author_email="mark.smith@mongodb.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
    extras_require=EXTRAS_REQUIRE,
)