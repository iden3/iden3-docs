# Iden3 Documentation FAQ

## Documentation sections
There are 4 major sections:

- **Technology** : White papers describing iden3 technology
	- Terminology
	- Services and Protocols
- **Developers** : Integration guides for developers
- **Repository Guide** : Copy of repository documentation from repos
	- Services and Infrastructure
	- ZKP
	- Misc
- **Publications** : Material published (pdf, presentations, videos,...)
	- Research Papers
	- Presentations
	- Videos

## Adding new doc to Technology

1. Create document (md or rst) in technology folder
2. Open *config/iden3_docmap.py*
3. Add document name to `iden3_tech_docs[‘docs’]`
   - Ex : document *claims.rst* is added as `technology/claims`
4. `Make doc html`
5. Check changes with browser in *build/html/index.html*


## Adding new doc to Developers

1.  Create document (md or rst) in devel folder (check existing doc *devel/centralized_login* to maintain consistent aspect)
2. Open *config/iden3_docmap.py*
3. Add document name to `iden3_devel_docs[‘docs’]`
   - Ex : document *centralized_log* is added as `technology/centralized_login`
4. `Make doc html`
5. Check changes with browser in *build/html/index.html*


## Adding docs from Repositories

1. Documents automatically collected from iden3 repos
   - `iden3_repo` variable in *config/iden3_docmap.py* contains current repos
   - If you need to add a new repo, copy existing mechanism (create dictionary with info on repo and add it to `iden3_repo` variable)
2. Explicitly adding document to  `docs` field allows you to control position of document (in order), and aspect (can add some directives in `prepend` field)
3. Adding document to `dont_publish` field will prevent that document from being published (internal, irrelevant,...)


## Merging docs from Repositories

1. Documents in repos can be merged if necessary
2. In *config/iden3_docmap.py*, modify `merged_docs` variable. Check existing example for more info.
   - `Main` : Add resulting document name
   - `Title` : Document title
   - `Docs` : Source documents in the order you want to merge them
   - `Prepend` :  *.rst* guidelines on how to show *.rst*  document. 
3. Make doc html
4. Check changes with browser in *build/html/index.html*

# Converting latex docs from repos to .rst
1. *.tex* documents in repos must be converted to *.rst* if you want them published. If not, don’t do anything. Check existing example for more info
2. In *config/iden3_docmap.py*, modify `latex_docs` variable
   - `Main` : Add resulting  *.rst*  document name
   - `Title` : Document title
   - `Docs` : Source *.tex* documents in 
   - `Biblio` : Source *.bib* doc containing bibliography. Add ‘’ if it doesn’t exist
   - `Prepend` :  *.rst* guidelines on how to show *.rst* document. 
   - `Pdf_link` :  you can add pdf document if you want to allow downloading. Pdf doc needs to be placed  in *iden3-docs/source/docs/*
3. Make doc html
4. Check changes with browser in *build/html/index.html*

# Adding new presentation to Publications
1. Presentations or pdf documents can be downloaded
2. Place document in *iden3-docs/source/docs/*
3. Edit *iden3-docs/source/docs/presentations.rst* and add directive to include link . Check existing examples 
4. Make doc html
5. Check changes with browser in *build/html/index.html*

# Adding new video to Publications 
1. Currently done with youtube videos only. If video file, repeat same procedure as adding a presentation. Check existing example for more info.
2. Edit *iden3-docs/source/docs/video.rst* and add directive to include video link 
3. Make doc html
4. Check changes with browser in *build/html/index.html*

