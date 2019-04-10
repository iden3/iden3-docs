# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SOURCEDIR     = source
BUILDDIR      = build

GITHUB_URL =  https://github.com/iden3

IDEN3JS_FOLDER = iden3js
GOIDEN3_FOLDER = go-iden3
WEBSNARK_FOLDER = websnark
SNARKJS_FOLDER = snarkjs
CITRUS_FOLDER = citrus
WASMBUILDER_FOLDER = wasmbuilder
NOTSERVER_FOLDER = notifications-server
DISCO_FOLDER = discovery-node
CIRCOM_FOLDER = circom
TXFORWARDER_FOLDER = tx-forwarder
CIRCOMLIB_FOLDER = circomlib
RESEARCH_FOLDER = research


aux_folders = $(IDEN3JS_FOLDER) \
              $(GOIDEN3_FOLDER) \
              $(WEBSNARK_FOLDER) \
              $(SNARKJS_FOLDER) \
              $(CITRUS_FOLDER) \
              $(WASMBUILDER_FOLDER) \
              $(NOTSERVER_FOLDER) \
              $(DISCO_FOLDER) \
              $(CIRCOM_FOLDER) \
              $(TXFORWARDER_FOLDER) \
              $(CIRCOMLIB_FOLDER) \
              $(RESEARCH_FOLDER)
              


AUX_FOLDERS := $(aux_folders)
# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	for j in $(AUX_FOLDERS); do git clone $(GITHUB_URL)/$$j.git ./$(SOURCEDIR)/$$j; done; fi
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
	for j in $(AUX_FOLDERS); do rm -rf $(SOURCEDIR)/$$j; done; fi
