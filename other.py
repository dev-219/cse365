import gzip
import shutil
#'/home/student/cse365/tarball/195/withkey/juliaplaintext.txt.gz.enc'
byte_ary = []
with open('/home/student/cse365/tarball/195/withkey/juliaplaintext.txt.gz.enc', 'rb') as f:
    byte_s = f.read(535)
    print(byte_s)

        