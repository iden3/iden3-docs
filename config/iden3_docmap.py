"""
/*
    Copyright 2018 0kims association.

    This file is part of cusnarks.

    cusnarks is a free software: you can redistribute it and/or
    modify it under the terms of the GNU General Public License as published by the
    Free Software Foundation, either version 3 of the License, or (at your option)
    any later version.

    cusnarks is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
    or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
    more details.

    You should have received a copy of the GNU General Public License along with
    cusnarks. If not, see <https://www.gnu.org/licenses/>.
*/

// ------------------------------------------------------------------
// Author     : David Ruiz
//
// File name  : iden3_docmap.py
//
// Date       : 26/04/2019
//
// ------------------------------------------------------------------
//
// Description:
//  Documentation configuration file
//
// ------------------------------------------------------------------

"""

# Main section descriptors : Developers, Technology, Publications
#  Repo guide is defined elsewhere
# index.rst references these 4 documents

iden3_devel_docs = {
               'folder': 'devel',                                   # Used to add tag
               'main'  :  'developers.rst',
               'sub_sections' : [''],
               'maxdepth' : [2],
               'hidden'   : [False],
               'caption'  : [False],
               'docs' : [
                          ['devel/centralized_login']
                        ],
               'alias' : ['Centralized Login'],
               'description' : [''],
}

iden3_tech_docs = {  
               'folder': 'technology', 
               'main'  : 'technology.rst',
               'sub_sections' : ['Terminology', 'Services & Protocols'],
               'maxdepth' : [1,1],
               'hidden'   : [False, False],
               'caption'  : ['', ''],
               'docs' : [
                          [
                           'technology/claims', 
                           'technology/identity' , 
                           'technology/merkle_tree',
                           'technology/zeroknowledge'
                          ],
                          [
                           'iden3js/src/protocols/login_merge',
                           'technology/claim_server',
                           'technology/ims_overview',
                           'technology/name_server',
                           'technology/identification_server',
                           'technology/notification_server',
                           'technology/relayer',
                           'technology/wallet'
                          ]
                        ]
}

iden3_publications_docs = {  
               'folder': 'publications', 
               'main'  : 'publications.rst',
               'sub_sections' : ['Research Papers','Presentations', 'Videos'],
               'maxdepth' : [1,1,1],
               'hidden'   : [False,False,False],
               'caption'  : ['','', ''],
               'docs' : [
                          [
                           'iden3_repos/research', 
                          ],
                          [ 
                            'docs/presentations'
                          ],
                          [ 
                            'docs/videos'
                          ],
                        ]
}

## Repo Description
iden3js_docs = {
   'url' : 'http://github.com/iden3/iden3js.git',
   'folder' : 'iden3js',
   'main'  : 'iden3js.rst',
   'sub_sections' : ['Iden3js'],
   'maxdepth' : [1],
   'hidden'   : [False],
   'caption'  : [False],
   'docs' : [
             [
              'iden3js/README'
             ],
            ],
   'prepend' : [ 
                  [
                    "========\nOverview\n========\n\n.. contents::    :depth: 3\n\n",
                  ],
                ],
   'dont_publish' : [
                      'iden3js/flow',
                     ]
}

goiden3_docs = {
   'url' : 'http://github.com/iden3/go-iden3.git',
   'folder' : 'go-iden3',
   'main'  : 'go-iden3.rst',
   'sub_sections' : ['Go-Iden3'],
   'maxdepth' : [1],
   'hidden'   : [False],
   'caption'  : [False],
   'docs' : [
             [
              'go-iden3/README',
              'go-iden3/merkletreeDoc/merkletree',
              'go-iden3/cmd/backupserver/README',
              'go-iden3/Relay',
              'go-iden3/crypto/README'
             ],
            ],
   'prepend' : [ 
                  [
                    "========\nOverview\n========\n\n.. contents::    :depth: 3\n\n",
                    "===========\nMerkle Tree\n===========\n\n.. contents::    :depth: 3\n\n",
                    "=============\nBackup Server\n=============\n\n.. contents::    :depth: 3\n\n",
                    "=====\nRelay\n=====\n\n.. contents::    :depth: 3\n\n",
                    "======\nCrypto\n======\n\n.. contents::    :depth: 3\n\n",
                  ],
                ],
   'dont_publish' : [ ]
}

tx_forwarder_docs = {
   'url' : 'http://github.com/iden3/tx-forwarder.git',
   'folder' : 'tx-forwarder',
   'main'  : 'tx-forwarder.rst',
   'sub_sections' : ['Tx Forwarder'],
   'maxdepth' : [1],
   'hidden'   : [False],
   'caption'  : [False],
   'docs' : [
             [
              'tx-forwarder/README',
             ],
            ],
   'prepend' : [ 
                  [
                    "========\nOverview\n========\n\n.. contents::    :depth: 3\n\n",
                  ],
                ],
   'dont_publish' : [ ]
}

circom_docs = {
   'url' : 'http://github.com/iden3/circom.git',
   'folder' : 'circom',
   'main'  : 'circom.rst',
   'sub_sections' : ['Circom'],
   'maxdepth' : [1],
   'hidden'   : [False],
   'caption'  : [False],
   'docs' : [
             [
              'circom/README',
              'circom/TUTORIAL',
             ],
            ],
   'prepend' : [ 
                  [
                    "========\nOverview\n========\n\n.. contents::    :depth: 3\n\n",
                    "========\nTutorial\n========\n\n.. contents::    :depth: 3\n\n",
                  ],
                ],
   'dont_publish' : [ ]
}

circomlib_docs = {
   'url' : 'http://github.com/iden3/circomlib.git',
   'folder' : 'circomlib',
   'main'  : 'circomlib.rst',
   'sub_sections' : ['CircomLib'],
   'maxdepth' : [1],
   'hidden'   : [False],
   'caption'  : [False],
   'docs' : [
             ['']
            ],
   'prepend' : [ 
                  [
                    '',
                  ],
                ],
   'dont_publish' : [
                      'circomlib/README' ]
}

websnark_docs = {
   'url' : 'http://github.com/iden3/websnark.git',
   'folder' : 'websnark',
   'main'  : 'websnark.rst',
   'sub_sections' : ['Websnark'],
   'maxdepth' : [1],
   'hidden'   : [False],
   'caption'  : [False],
   'docs' : [
             [
              'websnark/README',
             ],
            ],
   'prepend' : [ 
                  [
                    "========\nOverview\n========\n\n.. contents::    :depth: 3\n\n",
                  ],
                ],
   'dont_publish' : [ ]
}

discovery_node_docs = {
   'url' : 'http://github.com/iden3/discovery-node.git',
   'folder' : 'discovery-node',
   'main'  : 'discovery-node.rst',
   'sub_sections' : ['Discovery Node'],
   'maxdepth' : [1],
   'hidden'   : [False],
   'caption'  : [False],
   'docs' : [
             [
              'discovery-node/README',
             ],
            ],
   'prepend' : [ 
                  [
                    "========\nOverview\n========\n\n.. contents::    :depth: 3\n\n",
                  ],
                ],
   'dont_publish' : [ ]
}

citrus_docs = {
   'url' : 'http://github.com/iden3/citrus.git',
   'folder' : 'citrus',
   'main'  : 'citrus.rst',
   'sub_sections' : ['Citrus'],
   'maxdepth' : [1],
   'hidden'   : [False],
   'caption'  : [False],
   'docs' : [
             [
              'citrus/README',
             ],
            ],
   'prepend' : [ 
                  [
                    "========\nOverview\n========\n\n.. contents::    :depth: 3\n\n",
                  ],
                ],
   'dont_publish' : [ ]
}

snarkjs_docs = {
   'url' : 'http://github.com/iden3/snarkjs.git',
   'folder' : 'snarkjs',
   'main'  : 'snarkjs.rst',
   'sub_sections' : ['SnarkJS'],
   'maxdepth' : [1],
   'hidden'   : [False],
   'caption'  : [False],
   'docs' : [
             [
              'snarkjs/README',
             ],
            ],
   'prepend' : [ 
                  [
                    "========\nOverview\n========\n\n.. contents::    :depth: 3\n\n",
                  ],
                ],
   'dont_publish' : [ ]
}

notifications_server_docs = {
   'url' : 'http://github.com/iden3/notifications-server.git',
   'folder' : 'notifications-server',
   'main'  : 'notifications-server.rst',
   'sub_sections' : ['Notifications Server'],
   'maxdepth' : [1],
   'hidden'   : [False],
   'caption'  : [False],
   'docs' : [
             [
              'notifications-server/README',
             ],
            ],
   'prepend' : [ 
                  [
                    "========\nOverview\n========\n\n.. contents::    :depth: 3\n\n",
                  ],
                ],
   'dont_publish' : [ ]
}

wasmbuilder_docs = {
   'url' : 'http://github.com/iden3/wasmbuilder.git',
   'folder' : 'wasmbuilder',
   'main'  : 'wasmbuilder.rst',
   'sub_sections' : ['Web Assembly Builder'],
   'maxdepth' : [1],
   'hidden'   : [False],
   'caption'  : [False],
   'docs' : [
             [
               ''
             ],
            ],
   'prepend' : [ 
                  [
                    '',
                  ],
                ],
   'dont_publish' : [ 
                      'wasmbuilder/README',
                    ]
}

research_docs = {
   'url' : 'http://github.com/iden3/research.git',
   'folder' : 'research',
   'main'  : 'research.rst',
   'sub_sections' : [''],
   'maxdepth' : [1],
   'hidden'   : [False],
   'caption'  : [False],
   'docs' : [
             [
               'research/publications/zkproof-standards-workshop-2/baby-jubjub/baby-jubjub',
               'research/publications/zkproof-standards-workshop-2/merkle-tree/merkle-tree',
               'research/publications/zkproof-standards-workshop-2/ed-dsa/ed-dsa',
               'research/publications/zkproof-standards-workshop-2/pedersen-hash/pedersen',
             ],
            ],
   'prepend' : [ 
                  [
                    "===========\nBaby Jubjub\n===========\n\n.. contents::    :depth: 3\n\n",
                    "===========\nMerkle Tree\n===========\n\n.. contents::    :depth: 3\n\n",
                    "======\nED-DSA\n======\n\n.. contents::    :depth: 3\n\n",
                    "=============\nPedersen Hash\n=============\n\n.. contents::    :depth: 3\n\n",
                  ],
                ],
   'dont_publish' : [ 
                      'research/README',
                    ]
}




iden3_default_section = {
     'maxdepth' : [1],
     'hidden'   : [True],
     'caption'  : [False],
}

merged_docs = {
                'main'  : [
                            'iden3js/src/protocols/login_merge.rst',
                          ],
                'title' : [
                            'Login Protocol'
                          ],
                'docs' : [
                          [
                           'iden3js/src/protocols/login_spec', 
                           'iden3js/src/protocols/README',
                           'iden3js/src/protocols/login_spec_rationale',
                          ],
                         ],
                 'prepend' : [
                    ".. contents::    :depth: 3\n\n",
                        ]
}

latex_docs = {
               'main' : [
                          'research/publications/zkproof-standards-workshop-2/baby-jubjub/baby-jubjub.rst',
                          'research/publications/zkproof-standards-workshop-2/merkle-tree/merkle-tree.rst',
                          'research/publications/zkproof-standards-workshop-2/ed-dsa/ed-dsa.rst',
                          'research/publications/zkproof-standards-workshop-2/pedersen-hash/pedersen.rst',
                        ],
                'title' : [
                            'Baby Jub-jub',
                            'Merkle Tree',
                            'ED-DSA',
                            'Pedersen Hash',
                          ],
                'docs' : [
                           'research/publications/zkproof-standards-workshop-2/baby-jubjub/main.tex',
                           'research/publications/zkproof-standards-workshop-2/merkle-tree/standard.tex',
                           'research/publications/zkproof-standards-workshop-2/ed-dsa/standard.tex',
                           'research/publications/zkproof-standards-workshop-2/pedersen-hash/main.tex',
                         ],
                'biblio' : [
                           'research/publications/zkproof-standards-workshop-2/baby-jubjub/lit.bib',
                           'research/publications/zkproof-standards-workshop-2/merkle-tree/lit.bib',
                           'research/publications/zkproof-standards-workshop-2/ed-dsa/lit.bib',
                           'research/publications/zkproof-standards-workshop-2/pedersen-hash/lit.bib',
                           ],
                 'prepend' : [
                    ".. contents::    :depth: 3\n\n",
                    ".. contents::    :depth: 3\n\n",
                    ".. contents::    :depth: 3\n\n",
                    ".. contents::    :depth: 3\n\n",
                        ],
                  'pdf_link' : [ 
                              'Baby-Jubjub.pdf',
                              'MerkleTree.pdf',
                              'Ed-DSA.pdf',
                              'Pedersen-Hash.pdf',
                            
                               ]
}

iden3_repo = [ iden3js_docs, goiden3_docs, tx_forwarder_docs, 
               circom_docs, circomlib_docs, websnark_docs,
               discovery_node_docs, snarkjs_docs, notifications_server_docs,
               wasmbuilder_docs, research_docs ]                       

iden3_docs = [ iden3_devel_docs, iden3_tech_docs, iden3_publications_docs]

iden3_doc_source_folder = "./source"
iden3_doc_tmp_folder = "./source/tmp"
iden3_doc_template_folder = "./source/_templates"
iden3_doc_repo_folder = "./source/iden3_repos"
iden3_rst_filename = "./source/tmp/rst_list.txt"
iden3_tar_filename = "./source/iden3_repo_files.tgz"
iden3_doc_pdf_folder = "./source/docs"
