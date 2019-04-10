
import sys
import os

def build_tex(dirname):
   subdirs = [x[0] for x in os.walk(dirname)]
   prune_subdirs = [x for x in subdirs if ".git" not in x]
   for texdir in prune_subdirs:
       tex_files = [texdir+"/"+f for f in os.listdir(texdir) if f.endswith('.tex')]
       if len(tex_files) > 0:
         rst_file = texdir+'/'+get_fname(texdir)
         command = "pandoc " + ' '.join(tex_files) + " -o " + rst_file
         os.system(command)
         
def get_fname(x):
   rst_idx =  [s for s, v in enumerate(x) if v =='/']
   rst_file = x[rst_idx[-1]+1:]
   return rst_file+'.rst'

if __name__== "__main__":
  build_tex(sys.argv[1])
