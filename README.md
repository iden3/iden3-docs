# Iden3 Documentation

[![Website][website-shield]][docs.iden3.io]
[![Build Status][ci-shield]][ci]
[![Content License][content-license-shield]][content license]
[![License][license-shield]][license]
[![Master Version][master-version-shield]][releases]
[![Production Version][prod-version-shield]][releases]
[![Chat][chat-shield]][chat]

## Overview

This repository contains the source code and comment for the iden3 documentations website.

The website is generated and deployed using [readthedocs][].

The actual website is available at [**docs.iden3.io**][docs.iden3.io].

## Licensing

The content of this website is available under [CC BY-SA 4.0][content license].

The surrounding source code is available under [GPL-3.0][license].

*All contributions will fall under theses two licenses based on the type of contribution.*

## Building And Offline Use

*The documentation website can easily be built locally either for offline use or for [contribution][] purposes.*

1. Download/clone githup repository
   
   ``` shell
   git clone https://github.com/iden3/iden3-docs.git
   cd iden3-docs
   ```

2. Install [Readthedocs][install hugo] and dependencies
   ``` shell
   pip install -r requirements.txt
   ```

3. Build documentation

   ``` shell
   make html
   ```

4. Preview documentation in  build/html/index.html.

## Contributing

Anyone is welcome to contribute to the documentation by submitting pull requests to this repository.

*Please reade the [contribution guidelines][] first, to allow for smooth collaboration.*

[website-shield]: https://img.shields.io/website/http/docs.iden3.io.svg?down_color=red&down_message=offline&style=flat-square&up_color=green&up_message=online
[ci-shield]: https://img.shields.io/circleci/project/github/iden3/docs/master.svg?style=flat-square&maxAge=3600
[content-license-shield]: https://img.shields.io/github/package-json/contentLicense/iden3/docs.svg?style=flat-square&label=content&maxAge=3600
[license-shield]: https://img.shields.io/github/license/iden3/docs.svg?style=flat-square&maxAge=3600
[master-version-shield]: https://img.shields.io/github/package-json/v/iden3/docs/master.svg?label=latest&style=flat-square
[prod-version-shield]: https://img.shields.io/github/package-json/v/iden3/docs/production.svg?label=published&style=flat-square
[chat-shield]: https://img.shields.io/matrix/iden3:matrix.org.svg?style=flat-square&maxAge=3600&label=chat%20%28matrix%29
[docs.iden3.io]: https://docs.iden3.io
[ci]: https://circleci.com/gh/iden3/docs
[releases]: https://github.com/iden3/docs/releases
[chat]: https://matrix.to/#/#iden3:matrix.org
[readthedocs]: https://readthedocs.org
[circleci]: https://circleci.com/gh/iden3/docs
[github pages]: https://pages.github.com
[content license]: https://github.com/iden3/docs/blob/master/CONTENT_LICENSE
[license]: https://github.com/iden3/docs/blob/master/LICENSE
[install hugo]: https://gohugo.io/getting-started/installing
[hugo release]: https://github.com/gohugoio/hugo/releases/tag/v0.54.0
[contribution guidelines]: https://github.com/iden3/docs/blob/master/CONTRIBUTING.md
[contribution]: #Contributing
