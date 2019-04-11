# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SOURCEDIR     = source
BUILDDIR      = build
TEMPLATESDIR  = $(SOURCEDIR)/_templates

TEX2RST = pandoc
GITHUB_URL =  https://github.com/iden3
IDEN3REPOS_DIR = $(SOURCEDIR)/iden3_repos
IDEN3REPOS_FILES = iden3_repos_files.txt
IDEN3REPOS_TAR = iden3_repos_files.tgz
TMPREPO_DIR = tmp
IDEN3REPO_INDEX = repositories.rst
BUILDREPO_SCRIPT = build_repo.py

IDEN3JS_DIR = iden3js
GOIDEN3_DIR = go-iden3
WEBSNARK_DIR = websnark
SNARKJS_DIR = snarkjs
CITRUS_DIR = citrus
WASMBUILDER_DIR = wasmbuilder
NOTSERVER_DIR = notifications-server
DISCO_DIR = discovery-node
CIRCOM_DIR = circom
TXFORWARDER_DIR = tx-forwarder
CIRCOMLIB_DIR = circomlib
RESEARCH_DIR = research


aux_dirs = $(IDEN3JS_DIR) \
              $(GOIDEN3_DIR) \
              $(WEBSNARK_DIR) \
              $(SNARKJS_DIR) \
              $(CITRUS_DIR) \
              $(WASMBUILDER_DIR) \
              $(NOTSERVER_DIR) \
              $(DISCO_DIR) \
              $(CIRCOM_DIR) \
              $(TXFORWARDER_DIR) \
              $(CIRCOMLIB_DIR) 
              
aux_dirs_tex = $(RESEARCH_DIR)

AUX_DIRS := $(aux_dirs)
AUX_DIRS_TEX := $(aux_dirs_tex)
# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

repo:
	@if [ -d ./${TMPREPO_DIR} ]; then \
	    rm -rf ./${TMPREPO_DIR}; \
        fi 
	@if [ -d ./${IDEN3REPOS_DIR} ]; then \
	   rm -rf ./${IDEN3REPOS_DIR}; \
        fi
	@mkdir -p $(TMPREPO_DIR)
	@mkdir -p $(IDEN3REPOS_DIR)
	@for j in $(AUX_DIRS_TEX); do  \
	   git clone $(GITHUB_URL)/$$j.git ./$(TMPREPO_DIR)/$$j; \
	   python build_tex.py ./$(TMPREPO_DIR)/$$j; \
	done
	@cp $(TEMPLATESDIR)/$(IDEN3REPO_INDEX) $(SOURCEDIR)
	@for j in $(AUX_DIRS); do git clone $(GITHUB_URL)/$$j.git ./$(TMPREPO_DIR)/$$j; done; fi
	@find ./$(TMPREPO_DIR) -type f -name '*.md' > $(IDEN3REPOS_FILES)
	@find ./$(TMPREPO_DIR) -type f -name '*.rst' >> $(IDEN3REPOS_FILES)
	@python $(BUILDREPO_SCRIPT) $(IDEN3REPOS_FILES) $(IDEN3REPOS_DIR) >> $(SOURCEDIR)/$(IDEN3REPO_INDEX)
	@find ./$(TMPREPO_DIR) -type f -name '*.png' >> $(IDEN3REPOS_FILES)
	@tar -czf $(IDEN3REPOS_TAR) -T $(IDEN3REPOS_FILES)
	@tar  -C ./$(IDEN3REPOS_DIR)/ -xzf $(IDEN3REPOS_TAR)
	@mv ./$(IDEN3REPOS_DIR)/$(TMPREPO_DIR)/* ./$(IDEN3REPOS_DIR)
	@rm -rf $(TMPREPO_DIR) $(IDEN3REPOS_FILES) ./$(IDEN3REPOS_DIR)/$(TMPREPO_DIR) ./$(IDEN3REPOS_TAR)


.PHONY: help Makefile repo 

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
