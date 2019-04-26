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
// File name  : build_doc.py
//
// Date       : 25/04/2019
//
// ------------------------------------------------------------------
//
// Description:
//  Documentation builder functionality
//
// ------------------------------------------------------------------

"""

import sys
import os
import re

from iden3_docmap import *

def build_dir():
      command = "rm -rf " +iden3_doc_tmp_folder
      os.system(command)

      command = "rm -rf " +iden3_doc_repo_folder + "/*"
      os.system(command)

      command = "mkdir -p " + iden3_doc_tmp_folder
      os.system(command)

def download_repos():
   for repos in iden3_repo :
      command = "git clone " + repos['url'] + " " + iden3_doc_tmp_folder + "/" + repos['folder']
      os.system(command)

def find_files_bytype(ftype,folder):
   subdirs = find_dirs(folder)
   filtered_files = []
   for sd in subdirs:
      files = [sd+"/"+f for f in os.listdir(sd) if f.endswith('.'+ftype)]
      if len(files):
         filtered_files = filtered_files + files
 
   return filtered_files

def find_files_byname(fname, folder):
   subdirs = find_dirs(folder)
   filtered_files = []
   for sd in subdirs:
      files = [sd+"/"+f for f in os.listdir(sd) if fname in sd+"/"+f]
      if len(files):
         filtered_files = filtered_files + files
 
   return filtered_files

def find_dirs(folder):
   subdirs = [x[0] for x in os.walk(folder)]
   prune_subdirs = [x for x in subdirs if ".git" not in x]
   
   return prune_subdirs
 
def process_files(ftype):
   files = find_files_bytype(ftype, iden3_doc_tmp_folder)
   if ftype == 'md':
      pandoc_ftype = 'markdown'
      ext_idx = -3
   elif ftype == 'tex':
      pandoc_ftype = 'latex'
      ext_idx = -4
 
   for f in files:
     rst_file = f[:ext_idx] + '.rst'
     command = "pandoc -f " + pandoc_ftype + " -t rst " + f + " -o " + rst_file
     os.system(command)

def build_heading(heading_text,level):
    heading_len = len(heading_text)
    if level==1 or level==2:
       heading_marker = "="
    elif level==3:
       heading_marker = "#"
    elif level==4:
       heading_marker = "+"

    heading_marker = heading_marker * heading_len

    heading_string = "\n"
    if level==1:
       heading_string += heading_marker +"\n"
    
    heading_string += heading_text +"\n"
    heading_string += heading_marker +"\n"
   
    return heading_string


def add_heading(heading_text, level, fhandle):
    heading_string = build_heading(heading_text, level)
    fhandle.write(heading_string)

def add_toc(section,idx, fhandle):
    fhandle.write("\n")
    fhandle.write(".. toctree::\n")
    fhandle.write("   :maxdepth: " + str(section['maxdepth'][idx]) + "\n")
    if section['hidden'][idx]:
      fhandle.write("   :hidden:\n")
    if section['caption'][idx]:
      fhandle.write("   :caption: " + section['caption'][idx] + "\n")

def strip_dir(doc,base_dir):
    source_folder_len = len(base_dir)+1
    return doc[source_folder_len:]

def add_docs(section, base_dir, idx, fhandle):
    fhandle.write("\n")
    for doc in section['docs'][idx]:
      doc_list = find_files_byname(doc+".rst", iden3_doc_source_folder)
      if len(doc_list):
        doc = strip_dir(doc_list[0][:-4],base_dir)
        fhandle.write("   "+doc)
        fhandle.write("\n")

def append_to_file(string, fname):
      with open(fname,"a") as f:
         f.write(string)

def prepend_to_file(string, fname):
      with open(fname,"r+") as f:
         content = f.read()
         f.seek(0,0)
         f.write(string + content)

def process_docs(section, sub_idx):
   for prepend_string, rst_file in zip(section['prepend'][sub_idx], section['docs'][sub_idx]):
      if prepend_string != "":
          fname = iden3_doc_repo_folder + "/" + rst_file + ".rst"
          prepend_to_file(prepend_string, fname)
         
    
def add_listed_file_contents(section,base_dir,fhandle):       
   for sub_idx, sub_section_name in enumerate(section['sub_sections']):
      if sub_section_name != '':
         add_heading(sub_section_name,2,fhandle)
      add_toc(section,sub_idx,fhandle)
      add_docs(section,base_dir,sub_idx,fhandle)
      if 'prepend' in section:
         process_docs(section,sub_idx)

def add_unlisted_file_contents(repo, rst_files, base_dir, fhandle):
   folder = iden3_doc_tmp_folder + "/" + repo['folder']  
   tmp_folder_len = len(iden3_doc_tmp_folder) + 1
   for  files in rst_files:
     if folder in files:
        add_heading("Other",2,fhandle)      
        add_toc(iden3_default_section,0,fhandle)
        tmp_section = {'docs' : [[files[tmp_folder_len:-4]]] }
        add_docs(tmp_section,base_dir,0,fhandle)

def build_documentation():
   #Generate rst file from template
   base_dir = iden3_doc_source_folder
   for section in iden3_docs:
      fname = iden3_doc_source_folder + "/" + section['main']
      f = open(fname,"w")
      add_tag(section['folder'],f)
      f.write("\n")
      add_listed_file_contents(section, base_dir, f)

      f.close()

def get_dirname_from_fname(fname):
   idx =  [s for s, v in enumerate(fname) if v =='/']
   dirname = fname[:idx[-1]]
   return dirname
  
def get_fname(fname):
   idx =  [s for s, v in enumerate(fname) if v =='/']
   return_fname = fname[idx[-1]+1:]
   return return_fname

def build_download_link(string, link):
  return "\n:download:`"+string+" <" + link + ">`"

def build_latex_doc():
   curdir = os.getcwd()
   for docs_idx, doc in enumerate(latex_docs['main']):
      rst_fname = get_fname(iden3_doc_tmp_folder+"/"+doc)
      tex_fname = get_fname(iden3_doc_tmp_folder+"/"+latex_docs['docs'][docs_idx])
      bib_fname = get_fname(iden3_doc_tmp_folder+"/"+latex_docs['biblio'][docs_idx])
      tex_dirname = get_dirname_from_fname(iden3_doc_tmp_folder+"/"+latex_docs['docs'][docs_idx]) 
      os.chdir(tex_dirname)
      command="pandoc " + tex_fname + " -o " + rst_fname + " --bibliography " + bib_fname  
      os.system(command)
      append_to_file(build_heading("PDF Link", 2), rst_fname)
      append_to_file(build_download_link(latex_docs['title'][docs_idx],"./"+latex_docs['pdf_link'][docs_idx]),rst_fname)
      command = "cp " +curdir+"/"+iden3_doc_pdf_folder +"/" + latex_docs['pdf_link'][docs_idx] +" ."
      os.system(command)
      os.chdir(curdir)

      #content = read_document(tex_fname)
      #title_re = re.match("^(?!%)\\title{(.+)}",content)
      #if title_re:
        #print title_re.groups()

      #insert title and author
      #title_string = build_heading(title_heading, 1)
      #author_string =  build_heading(author_heading, 1)
      #doc_string = title_string + author_string 
      #prepend_to_file(doc_string, rst_fname)
  

   return

def build_repo_doc(rst_files):
   for repo in iden3_repo:
       fname = iden3_doc_repo_folder + "/" + repo['main']
       base_dir = iden3_doc_source_folder + "/iden3_repos"
       f = open(fname,"w")
       add_tag(repo['folder'],f)
       add_listed_file_contents(repo, base_dir, f)
       add_unlisted_file_contents(repo, rst_files, base_dir, f)

       f.close()
     

def add_tag(tag, fhandle):
  final_tag = '.. _'+tag+":"
  fhandle.write(final_tag)
  fhandle.write("\n")

def filter_files_docs(file_list,docs=None):
   for sections in iden3_repo + iden3_docs:
      docs = sum(sections['docs'],[])
      docs = [iden3_doc_tmp_folder+"/" + d + ".rst" for d in docs]
      file_list = [d for d in file_list if d not in docs]
      
   return file_list

def filter_files_blacklist(file_list):
   for sections in iden3_repo  :
      docs = sections['dont_publish']
      if len(docs):
        docs = [iden3_doc_tmp_folder+"/" + d + ".rst" for d in docs]
        file_list = [d for d in file_list if d not in docs]
      
   return file_list

def copy_files(files_to_copy):
    f = open(iden3_rst_filename,"w")
    for filename in files_to_copy:
      f.write(filename)
      f.write("\n")

    f.close()

    command = "tar -czf " + iden3_tar_filename + " -T " + iden3_rst_filename
    os.system(command)

    command = "tar -C " + iden3_doc_repo_folder +"/ -xzf " +iden3_tar_filename
    os.system(command)

    command = "mv " + iden3_doc_repo_folder + "/" + iden3_doc_tmp_folder +"/* " + iden3_doc_repo_folder  
    os.system(command)

    command = "rm -rf " + iden3_doc_tmp_folder 
    os.system(command)

    os.remove(iden3_tar_filename)

def read_document(fname):
    t = open(fname,"r")
    content = t.read()
    t.close()
    return content

def merge_documents():
  for doc_idx, doc in enumerate(merged_docs['main']):
       f = open(iden3_doc_tmp_folder+"/"+doc,"w")
       add_heading(merged_docs['title'][doc_idx],1,f)
       if merged_docs['prepend'][doc_idx] is not '':
          f.write("\n")
          f.write(merged_docs['prepend'][doc_idx])
          f.write("\n")

       for parts in merged_docs['docs'][doc_idx]:
          content = read_document(iden3_doc_tmp_folder+"/"+parts+".rst")
          os.remove(iden3_doc_tmp_folder+"/"+parts+".rst")
          f.write("\n")
          f.write(content)
 
       f.close()
    
def build_iden3_doc():
  # Build dir structure
  build_dir()

  # Download Repos
  download_repos()

  # Proceess .md files
  process_files("md")

  build_latex_doc()

  merge_documents()

  # Generate .rst list
  rst_files = find_files_bytype("rst", iden3_doc_tmp_folder)
  pdf_files = find_files_bytype("pdf", iden3_doc_tmp_folder)
  rst_files = filter_files_blacklist(rst_files)
  png_files = find_files_bytype("png", iden3_doc_tmp_folder)
  copy_files(rst_files + png_files + pdf_files)

  rst_files = filter_files_docs(rst_files)
 
  build_repo_doc(rst_files)

  # Build documentation folder
  build_documentation()

                     
                  
if __name__== "__main__":
   build_iden3_doc()
      
