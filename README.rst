===============
Tokenizer Tools
===============


.. image:: https://img.shields.io/pypi/v/tokenizer_tools.svg
        :target: https://pypi.python.org/pypi/tokenizer_tools

.. image:: https://travis-ci.com/howl-anderson/tokenizer_tools.svg?branch=master
        :target: https://travis-ci.com/howl-anderson/tokenizer_tools

.. image:: https://readthedocs.org/projects/tokenizer-tools/badge/?version=latest
        :target: https://tokenizer-tools.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


.. image:: https://pyup.io/repos/github/howlandersonn/tokenizer_tools/shield.svg
     :target: https://pyup.io/repos/github/howlandersonn/tokenizer_tools/
     :alt: Updates



Tools/Utils for NLP (including dataset reading, tagset encoding & decoding, metrics computing) | NLP 工具集（包含数据集读取、tagset 编码和解码、指标的计算等）


* Free software: MIT license
* Documentation: https://tokenizer-tools.readthedocs.io.


Features
--------

* 常见数据集格式的读取
* 多种 Tagset 的编码和解码
* 指标的计算

功能
----

语料集读写
^^^^^^^^^^^
本软件提供了一种语料存储的磁盘文件格式（暂定名为 conllx）和内存对象格式（暂定名为 offset）。

语料集读取
"""""""""""
任务：读取 corpus.collx 文件，遍历打印每一条语料。

代码：

.. code-block:: python

    from tokenizer_tools.tagset.offset.corpus import Corpus

    corpus = Corpus.read_from_file("corpus.conllx")
    for document in corpus:
        print(document)  # document 就是单条语料对象

语料集写入
"""""""""""
任务：将多条语料写入 corpus.conllx 文件

代码：

.. code-block:: python

    corpus_list = [corpus_item_one, corpus_item_two]

    corpus = Corpus(corpus_list)
    corpus.write_to_file("corpus.conllx")

语料属性和方法
^^^^^^^^^^^^^^^^^
每一个单条语料都是一个 offset sequence 对象，现在介绍这个对象所拥有的属性和方法

属性
""""""
TODO

方法
""""
TODO

TODO
-----

* 改变项目的名字，tokenizer_tools 已经无法正确描述现在项目的功能

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
