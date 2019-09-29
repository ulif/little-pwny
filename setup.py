from setuptools import setup

setup(
        name="pwpwnd",
        version="0.1.dev0",
        description="Check whether your password has been pwnd",
        url="https://github.com/ulif/pwpwnd",
        author="ulif",
        author_email="uli@gnufix.de",
        license="GPL3",
        packages=["pwpwnd"],
        zip_safe=False,
        entry_points={
            'console_scripts': ['pwpwnd = pwpwnd:main']}
        )

