# Contributing To The Iden3 Docs

:tada: First, thank you for taking the time to contribute to Iden3 :tada:

> **Note:** If you just have a question or need help with Iden3, please send us a message via [our matrix chat][chat]. 
> Issues for support requests will be closed.
>
> **Note:** If you want to report bug or contribute to any of the software written by Iden3, 
> please open an issue or a pull request directly on the software's repository.
> The maintainer of the software may not check the issues in the docs, and your issue may be left open **indefinitely**.

## Submitting Content

If you want to improve or add to the documentation and specifications for Iden3, you are in the right place! :tada:

> You will need [hugo][] and [npm][] to properly build the the website and run all the checks locally
> ([install hugo][hugo-install], [install npm][npm-install]).

1. [Fork][fork] the [docs repository][].

2. Add your changes:
   
   - To edit an existing page simply modify the corresponding markdown file in `<category>/<page-name>.md`.
   
   - To add new content simply run:
     ``` shell
     hugo -s docs new "<category>/<page-name>.md"
     ```
     
   Where `<category>` is one of the categories: `getting-started`, `documentation` or `specfications`,
   and `<page-name>.md` is the name of the page you want to add.     
   
   > **Note:** Don't forger to edit the [front matter][].

3. Make sure all the checks pass using:

   ``` shell
   npm run check
   ```

4. Make sure you don't break anything. 
   Run the following command and go to `http://localhost:1313` to check that the site looks correct.
   
   ``` shell
   npm run develop
   ```

5. Document your changes in `CHANGELOG.md` under the [Unreleased section][changelog-unreleased].

6. Write a [good commit messages][]:

   - Capitalized, short (50 chars or less) summary
   - Optionally, one blank line followed by a more detailed explanation

7. Submitted your changes via a [pull request (PR)][pr] from your fork of the repository 
   against the [`master`][master] branch and detail the changes in the description.

8. Make sure your pull request is up to date with [`master`][master].

### Front Matter

You can edit the front matter as needed:

- Set `draft = true` for new pages to make sure the page is not accidentally be published.
  (Draft status will be removed before a deployment by a maintainer)
  
  > **Note:** You may also submit a draft (with `draft = true`) to make sure it your changes are included upstream,
  > without publishing them before they are ready. 
  > But please, avoid spamming with draft pull requests and *do not mark as draft an already published page*.  

- Set `math = true` to use math notation using [katex][].  

  > **Note:** Please do not enable math rendering if you do not have math notation on that specific page.

- Set `weight = <value>` to set the position of the page among its siblings

  > **Note:** You may have to change the weight of the siblings pages as well.

- Edit the `title` as needed.

- Edit or remove the `subtitle` as needed.

## Discuss Improvements And New Content

If you are not sure about the improvements you want to submit, please [open an issue][issue-new] first to discuss it.
Don't forget to check if [an issue is already open][issues].

> **Note:** You do not have to open an issue first but in this case 
> *be ready to have your pull requested remained open indefinitely or closed and your changes left unmerged*,
> if your changes do not align with the current work and docs of Iden3.

[docs repository]: https://github.com/iden3/docs
[master]: https://github.com/iden3/docs/commits/master
[issues]: https://github.com/iden3/docs/issues
[issue-new]: https://github.com/iden3/docs/issues/new
[pr]: https://github.com/iden3/docs/compare
[changelog-unreleased]: CHANGELOG.md#Unreleased
[front matter]: #front-matter
[chat]: https://matrix.to/#/#iden3:matrix.org
[hugo]: https://gohugo.io/
[hugo-install]: https://gohugo.io/getting-started/installing/
[npm]: https://www.npmjs.com/
[npm-install]: https://docs.npmjs.com/downloading-and-installing-node-js-and-npm
[good commit messages]: https://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html
[fork]: https://help.github.com/en/articles/fork-a-repo
[katex]: https://katex.org/
