import sys

def build_repo(filename, repodir):
  f = open(filename,'r')
  f1 = f.readlines()
  prev_repo = " "
  section = ""
  n_lines = 0
  for x in f1:
      new_x = change_basedir(x, repodir)
      repo = get_repo(new_x)
      if repo != prev_repo:
         print section
         prev_repo = repo
         print repo.title()
         print len(repo)*"="
         print ".. toctree::\n   :maxdepth: 1\n\n"
         section = "" 
         n_lines = 0
      n_lines +=1
      section = section + "\n   " + new_x
  print section
  f.close()

def get_repo(x):
   repo_idx =  [s for s, v in enumerate(x) if v =='/']
   repo = x[repo_idx[0]+1:repo_idx[1]]
   return repo
   
def change_basedir(x, newdir):
   dst_idx =  [s for s, v in enumerate(newdir) if v =='/']
   dst_dir = newdir[dst_idx[0]+1:]
   src_idx =  [s for s, v in enumerate(x) if v =='/']
   src_dir = dst_dir + '/' + x[src_idx[1]+1:]
   return src_dir
   

if __name__== "__main__":
  build_repo(sys.argv[1], sys.argv[2])
