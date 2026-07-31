from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="dmit-brainprint-analytics",
    version="1.0.0",
    author="DMIT.fyi — Merit Teacher",
    author_email="info@dmit.fyi",
    description="DMIT BrainPrint Analytics is an intelligent assessment platform for fingerprint analysis, cognitive profiling, learning preferences, personality insights, and career guidance.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://dmit.fyi",
    project_urls={
        "Homepage": "https://dmit.fyi",
        "GitHub": "https://github.com/dmit-fyi/dmit-brainprint-analytics",
        "Documentation": "https://dmit-brainprint-analytics.readthedocs.io",
        "PyPI": "https://pypi.org/project/dmit-brainprint-analytics",
    },
    py_modules=["brainprint"],
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Education",
        "Topic :: Scientific/Engineering :: Information Analysis",
    ],
    keywords=[
        "dmit",
        "dermatoglyphics",
        "multiple-intelligence",
        "fingerprint-analysis",
        "brainprint",
        "cognitive-profiling",
        "career-guidance",
        "dmit-fyi",
    ],
    entry_points={
        "console_scripts": [
            "dmit-brainprint=brainprint:main",
        ],
    },
)
