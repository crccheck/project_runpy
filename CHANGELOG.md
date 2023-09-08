# CHANGELOG



## v1.1.0 (2023-09-08)

### Chore

* chore: Add semantic-release process (#23) ([`4908db4`](https://github.com/crccheck/project_runpy/commit/4908db45931ba3d6c2563e9536d309782b68deaf))

### Feature

* feat: collapse whitespace in multiline sql (#20)

When used in conjunction with the colorizing output, only the first line of the SQL is colored. This is due to the logging filter assuming anything after the first line is a traceback; something to present in without color. Unfortunately, this breaks the intent of the SQL logging.

Linebreaks in SQL logging aren&#39;t important. Getting rid of them doesn&#39;t hurt readability. In fact, even without the colorization, readability is improved because more lines fit on one screen.

This does not catch all SQL with line breaks... I&#39;ll have to update the logic again later if I care. ([`64c3ca9`](https://github.com/crccheck/project_runpy/commit/64c3ca9ed3474ae3dc1b8839902cbe2b448f8f3d))

* feat(ci): add Github Actions instead of TravisCI (#18) ([`5e18211`](https://github.com/crccheck/project_runpy/commit/5e18211eb77e76c4b1613a16addacf26b3c0e0e2))

### Fix

* fix: Github is stupid ([`94202c0`](https://github.com/crccheck/project_runpy/commit/94202c0dbd7bfc698380b152cd4cf72eaa380748))

### Refactor

* refactor: consolidate config in pyproject.toml (#22)

and some basic maintenance on lint checking ([`9064e17`](https://github.com/crccheck/project_runpy/commit/9064e17fa4542adbb02720f6c21411ea215196cf))

* refactor: enforce Black lint style in CI and delint (#19) ([`d1e475f`](https://github.com/crccheck/project_runpy/commit/d1e475f8e06a49ffc27dbbe23f715da5879ffb53))

### Unknown

* add ColorizingNameStreamHandler to color based on logger name (#21) ([`4b5113c`](https://github.com/crccheck/project_runpy/commit/4b5113c29fa86c9a3ccac6290533baf24903594f))


## v1.0.1 (2019-11-14)

### Fix

* fix(heidi): fix when there&#39;s no sql to format (#17)

When no `sql` is passed into the logger, the formatter double fails and throws it&#39;s own error. That&#39;s no good. This fixes it by making sure there&#39;s `sql` to format.

Fixes #16 ([`7301bd2`](https://github.com/crccheck/project_runpy/commit/7301bd23b23351589f87a454b859fbe32d9f40cc))

### Unknown

* 1.0.1 ([`4a0d66b`](https://github.com/crccheck/project_runpy/commit/4a0d66bfa88e611ddd8dfc68cc75227d451ca692))


## v1.0.0 (2019-07-09)

### Breaking

* feat: Update to Django v2 and drop Python2 support (#15)

BREAKING CHANGE: Django 2&#39;s sql logging format is different, so we need to adapt. Python 2 is also dead to me, so dropping support for that. ([`3c0c4f0`](https://github.com/crccheck/project_runpy/commit/3c0c4f030089292ad9886f88187a1ab8ab77a5f3))

### Unknown

* 1.0.0 ([`b70c8b4`](https://github.com/crccheck/project_runpy/commit/b70c8b4dc398411a02905ad7c97db388ace9e4fd))


## v0.4.0 (2019-07-09)

### Breaking

* chore: Update Python versions (#12)

BREAKING CHANGE: Drops Python 2.6 support, Updates Python 3 support

* Drops Tox in favor of vanilla Travis CI
* Drops Coverage in CI because it needs modernizing ([`e40a1b1`](https://github.com/crccheck/project_runpy/commit/e40a1b1599fb55139a47a95c115daa15dc4a8904))

### Chore

* chore: Change publishing to use Flit (#13)

Flit is a well-maintained package that removes a lot of the hassle around publishing to PyPI. The current `setup.py` was out of date, and migrating to Flit was easier than updating everything.

https://flit.readthedocs.io/en/latest/index.html ([`4af0ccf`](https://github.com/crccheck/project_runpy/commit/4af0ccf87fcf7c9dbf37670cc529d2f85bf21a71))

### Feature

* feat: add local test coverage (#14)

I didn&#39;t re-enable Coveralls because it looks like they haven&#39;t caught up to the new TravisCI build stages config and I&#39;m too lazy to figure it out on my own. ([`b62f4cf`](https://github.com/crccheck/project_runpy/commit/b62f4cf7c4facca0e75118e98ab119e1cb42e5ce))

### Unknown

* 0.4.0 ([`6d07c5f`](https://github.com/crccheck/project_runpy/commit/6d07c5fd3c8c41c8d52f059fe038f1b09dcc4021))

* Simpler and shorter sql formatting (#10)

Get shorter, more consistent output at the expense of computation and some loss of info

Kind of a throwaway PR because this is so old it won&#39;t work with Django 2+, but gonna merge anyways to get more testing and to do a test `flit` release ([`f38eea8`](https://github.com/crccheck/project_runpy/commit/f38eea8e6cbc41543a726330a9d32a1e80be1cdb))

* Merge pull request #7 from crccheck/dj17-sql-logging

fix readable sql filter did not work with django 1.7 ([`00850be`](https://github.com/crccheck/project_runpy/commit/00850be1075c38484e5a90fdfd27fd89ec361be8))

* fix readable sql filter did not work with django 1.7 ([`9fe7ec4`](https://github.com/crccheck/project_runpy/commit/9fe7ec4c0ddd3f6711f08bf20608b74fc29130d3))


## v0.3.1 (2014-08-18)

### Unknown

* bump version to 0.3.1 ([`097b908`](https://github.com/crccheck/project_runpy/commit/097b908ac3924f6fac88701e5e6e5c9f6b5be794))

* Merge pull request #4 from crccheck/sql-filter-fix

fix how not every SELECT has a FROM ([`3a952af`](https://github.com/crccheck/project_runpy/commit/3a952afcf42d6f4c9f3e62fc9a834dcdb74f1b34))

* add better coverage to sql filter ([`c8bae21`](https://github.com/crccheck/project_runpy/commit/c8bae21428c707a32e66528223378bf7630c1c8b))

* Merge remote-tracking branch &#39;origin/master&#39; into sql-filter-fix ([`c6c1133`](https://github.com/crccheck/project_runpy/commit/c6c11330f8f944dffc9fb0abed909a2b692196dc))

* Merge pull request #5 from crccheck/testing

Modernize Testing ([`a78e529`](https://github.com/crccheck/project_runpy/commit/a78e529d6997014117fc71b671efacd4ed8d0359))

* doc env.get to try and sell it a little better ([`106d3f7`](https://github.com/crccheck/project_runpy/commit/106d3f7bac726ec43cb293c158a2c6c36d34ac7f))

* doc similarity to dj debug toolbar ([`17f33e8`](https://github.com/crccheck/project_runpy/commit/17f33e89cf802991ef4a2d14f4d57d16bb9e8c15))

* rename test module to something less generic ([`d6fa119`](https://github.com/crccheck/project_runpy/commit/d6fa119acd019d14c8338e20d4aae402eac45deb))

* add __version__ attribute ([`0bdb5a0`](https://github.com/crccheck/project_runpy/commit/0bdb5a0aa902b94599c35c765d3019c8c56aed7c))

* add support for wheels ([`25d357d`](https://github.com/crccheck/project_runpy/commit/25d357d684fede28fe35c7253819537e8556a123))

* badges badges badges badges mushroom mushrrom ([`117ed5e`](https://github.com/crccheck/project_runpy/commit/117ed5e1e0c703bd9b800d9ec103a1eb2b5baa2c))

* add travis-ci and coveralls integration ([`6da5b78`](https://github.com/crccheck/project_runpy/commit/6da5b78c3428a89ae8fedbbaeaaa94f5fa4bfb8e))

* add coverage runner to tox ([`9f29374`](https://github.com/crccheck/project_runpy/commit/9f29374c82230a3d9eafc3911aa4dc51f7962c61))

* add coverage support ([`7933542`](https://github.com/crccheck/project_runpy/commit/79335425c6d83e069eba85dfd7422682ea978fcd))

* add python 3.4 to list of supported versions ([`3b54c58`](https://github.com/crccheck/project_runpy/commit/3b54c583bce0b39dfc35f83b86e2259f0ed23e3d))

* remove nose as a requirement for testing ([`5a9fd47`](https://github.com/crccheck/project_runpy/commit/5a9fd47a817be7a07a9a9feca429499531286cdf))

* Merge pull request #3 from crccheck/remove-project_dir

delete never used project_dir functionality ([`1827118`](https://github.com/crccheck/project_runpy/commit/18271181dbe5e575af0af13fb5a4d8f293b66b51))

* delete never used project_dir functionality

I found another package that does the same thing, but I can&#39;t remember
the name :( it was in some django settings guide. ([`97d32fe`](https://github.com/crccheck/project_runpy/commit/97d32fec544d34becc5ea33a9f8a9f6e37ae2f97))

* fix how not every SELECT has a FROM ([`f1577b4`](https://github.com/crccheck/project_runpy/commit/f1577b4b2e82b243a0470df42c9e47229a5be5f7))


## v0.3.0 (2014-01-27)

### Unknown

* Merge branch &#39;required&#39; (v0.3.0) ([`6c00d45`](https://github.com/crccheck/project_runpy/commit/6c00d4549c658c50140b64051d8ba29238a2f168))

* add a wrapper around env.get for required env

closes #2 ([`1fae2dd`](https://github.com/crccheck/project_runpy/commit/1fae2dd6954f594c90e58d68c0628090fa3bf7c8))


## v0.2.0 (2014-01-27)

### Unknown

* Merge branch &#39;sqlfilter&#39; (v0.2.0) ([`06d9e2c`](https://github.com/crccheck/project_runpy/commit/06d9e2c5ffb060627dfffd3eec96c1d819858b33))

* add light test coverage of ReadableSqlFilter ([`b1f7eaf`](https://github.com/crccheck/project_runpy/commit/b1f7eaf3a0c27c97a13bffbaa27cf14a2b22c357))

* make distinction between running tests and tox ([`8d1edea`](https://github.com/crccheck/project_runpy/commit/8d1edeac2c9b4baab9e0d8408846d588d781d5ea))

* add light coverage to ColorizingStreamHandler ([`33d7d8e`](https://github.com/crccheck/project_runpy/commit/33d7d8e548e65c8b05a19aced06f949556fa2c89))

* add documentation to readme ([`cedd7bf`](https://github.com/crccheck/project_runpy/commit/cedd7bf2f92c1809f9158990ed0e775e333eec7b))

* add my sql logging filter ([`bdc538f`](https://github.com/crccheck/project_runpy/commit/bdc538f37f69631c4b98665367f6d6a8441e0606))


## v0.1.1 (2013-06-07)

### Unknown

* bump to version 0.1.1

bugfixes:

* fixes typos in readme
* fixes bad import style ([`db44f28`](https://github.com/crccheck/project_runpy/commit/db44f28d9839c1cb049ce28f9aa5e82758185c99))

* expand tox coverage to python 3.3 and finish up ([`eb02897`](https://github.com/crccheck/project_runpy/commit/eb02897bce1e7285be9a73c5e890c343d9cd1af5))

* fix package was not using relative imports ([`104414e`](https://github.com/crccheck/project_runpy/commit/104414e1fe8b8d8b46f37202c76f46d43d8e4130))

* expand tox coverage to python 2.6 ([`249ddc8`](https://github.com/crccheck/project_runpy/commit/249ddc8b29706283b804d3adbee4deebcb3cb55b))

* add tox.ini ([`9800a73`](https://github.com/crccheck/project_runpy/commit/9800a733219e1d05b6cca46791b3e8ea52b9d80d))

* fix typos in readme ([`a7b746f`](https://github.com/crccheck/project_runpy/commit/a7b746f66bb6c1b4fe785b38d201e4e16377a1e9))


## v0.1.0 (2013-06-06)

### Unknown

* bump to version 0.1.0 ([`3c28da2`](https://github.com/crccheck/project_runpy/commit/3c28da22fedf3a169606c3a8be04627dcaa776f3))

* write a README ([`0918fa8`](https://github.com/crccheck/project_runpy/commit/0918fa8db2f3dc0a2ba9c3c95248c5f544282c9b))

* make all utils available at base package level ([`46a7857`](https://github.com/crccheck/project_runpy/commit/46a785760444b47a069ede69fe00dd160f4cf7f1))

* add make build/ make all command ([`89498cd`](https://github.com/crccheck/project_runpy/commit/89498cd1f80a0314d45096e2ff08a748bfd8d517))

* switch back to distutils, not using install_requires ([`c30769a`](https://github.com/crccheck/project_runpy/commit/c30769a393e74a4613608fc82a7c910798fcb8cc))

* update syntax of project dir helper ([`a38a459`](https://github.com/crccheck/project_runpy/commit/a38a459b376d92e5ac6cc29b3b7bca6ce29efed7))

* fix type was no coerced if no standard default ([`45188c3`](https://github.com/crccheck/project_runpy/commit/45188c3b3bf3ead4522ccf3ff28f28bef4ec73b5))

* implement env ([`d0a77ae`](https://github.com/crccheck/project_runpy/commit/d0a77ae2b6ab49a793daeaefd324b2595e8497dc))

* merge get_env and env.get ([`5f6a206`](https://github.com/crccheck/project_runpy/commit/5f6a206659e40ee83cc41c330157866d840241a7))

* kill the docstrings until new syntax is found ([`00fdd3e`](https://github.com/crccheck/project_runpy/commit/00fdd3e2aa1f2f5418c11c16c89e0d52bf859b33))

* fork dj-settings-helper&#39;s utils ([`c327ee9`](https://github.com/crccheck/project_runpy/commit/c327ee965107b7a702e5ffc2c7cd781e3417695a))

* update make clean to grab pyc and ds_store ([`937d79f`](https://github.com/crccheck/project_runpy/commit/937d79fb46e0047b515923bdb3c7b51b7b1b7bef))

* add &#39;make clean&#39; ([`6983156`](https://github.com/crccheck/project_runpy/commit/6983156c3ec2bd9a96295997d23743c54e20d502))

* add basic readme ([`9b23266`](https://github.com/crccheck/project_runpy/commit/9b23266b34bb94c47bbe28478fffe0c91e97e4c0))

* add helper to heidi ([`5490c3a`](https://github.com/crccheck/project_runpy/commit/5490c3aca8b98cbe5a943c7bc34134666b92db7c))

* add helpers to tim ([`6222a51`](https://github.com/crccheck/project_runpy/commit/6222a511fd15b3b335c1fdde764ec68756a7ccfb))

* initial skeleton ([`3e3c0f7`](https://github.com/crccheck/project_runpy/commit/3e3c0f7161ca3cab24d9d81ac9859d2bdcab834d))

* initial commit (empty) ([`68b1c0e`](https://github.com/crccheck/project_runpy/commit/68b1c0e48c8822411a38f14d6788d11127c984f5))
