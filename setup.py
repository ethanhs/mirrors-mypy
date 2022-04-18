from __future__ import annotations

from setuptools import setup


setup(
    name='pre_commit_placeholder_package',
    version='0.0.0',
    install_requires=['mypy @ git+https://github.com/python/mypy.git@9cab2964a186d7e71567a1528fcc956f9eecebac'],
)
