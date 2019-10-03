from setuptools import setup

setup(
        name="pwny",
        version="0.1.dev0",
        description="Check whether your password has been pwnd",
        url="https://github.com/ulif/pwny",
        author="ulif",
        author_email="uli@gnufix.de",
        license="GPL3",
        packages=["pwny"],
        zip_safe=False,
        entry_points={
            'console_scripts': ['pwny = pwny:main']}
        )

