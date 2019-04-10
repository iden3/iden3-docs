# Iden3 Documentation

[![Website][website-shield]][docs.iden3.io]
[![Build Status][readthedocs-shield]][readthedocs-docs]

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

1. Download/clone github repository
   
   ``` shell
   git clone https://github.com/iden3/iden3-docs.git
   cd iden3-docs
   ```

2. Install [Readthedocs][install readthedocs] and dependencies
   ``` shell
   pip install -r requirements.txt
   ```

3. Build documentation

   ``` shell
   make html
   ```

4. Preview documentation in located in build/html/index.html.

## Contributing

Anyone is welcome to contribute to the documentation by submitting pull requests to this repository.

*Please read the [contribution guidelines][] first, to allow for smooth collaboration.*

[website-shield]: https://img.shields.io/website/http/docs.iden3.io.svg?down_color=red&down_message=offline&style=flat-square&up_color=green&up_message=online
[readthedocs-shield]: https://readthedocs.org/projects/pip/badge/
[docs.iden3.io]: https://docs.iden3.io
[readthedocs-docs]: https://iden3-docs.readthedocs.io
[readthedocs]: https://readthedocs.org
[content license]: https://github.com/iden3/iden3-docs/blob/master/CONTENT_LICENSE
[license]: https://github.com/iden3/iden3-docs/blob/master/LICENSE
[install readthedocs]: https://docs.readthedocs.io/en/stable/intro/getting-started-with-sphinx.html
[contribution guidelines]: https://github.com/iden3/iden3-docs/blob/master/CONTRIBUTING.md
[contribution]: #Contributing
