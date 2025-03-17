from setuptools import setup, find_packages

setup(
    name="wakeword_detector",  # Package name
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="An open-source wake-word detection package using PyTorch",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/wakeword-detection/wakeword-detector",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "torch",
        "torchaudio",
        "numpy",
        "librosa",
        "scipy",
        "sounddevice",
        "matplotlib",
        "scikit-learn"
    ],
    entry_points={
        "console_scripts": [
            "wakeword-record=wakeword_detector.record:main",
            "wakeword-detect=wakeword_detector.detect:main"
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)

