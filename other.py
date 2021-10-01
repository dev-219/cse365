import gzip
import shutil
with gzip.open('/home/student/cse365/tarball/195/withkey/juliaplaintext.txt.gz.enc', 'rb') as f_in:
    with open('output2.txt', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)
        