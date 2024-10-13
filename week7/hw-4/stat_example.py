import grp
import os
from pathlib import Path
import pwd
import sys

from stat import S_ISBLK, S_ISCHR, S_ISDIR, \
    S_ISDOOR, S_ISGID, S_ISLNK, S_ISREG, \
    S_ISSOCK, S_ISUID, S_ISVTX, S_IXGRP, S_IXOTH, S_IXUSR


def file_type_letter(mode: int) -> int:
    c = '?'

    if S_ISREG(mode):
        c = '-'
    elif S_ISDIR(mode):
        c = 'd'
    elif S_ISBLK(mode):
        c = 'b'
    elif S_ISCHR(mode):
        c = 'c'
    elif S_ISLNK(mode):
        c = 'l'
    elif S_ISSOCK(mode):
        c = 's'
    elif S_ISDOOR(mode):
        c = 'D'

    return c


def ls_perms(mode: int) -> str:
    rwx = ["---", "--x", "-w-", "-wx",
           "r--", "r-x", "rw-", "rwx"]

    bits = [0] * 10

    bits[0] = file_type_letter(mode)
    bits[1] = rwx[(mode >> 6) & 7]
    bits[4] = rwx[(mode >> 3) & 7]
    bits[7] = rwx[(mode & 7)]

    if mode & S_ISUID:
        bits[3] = 's' if (mode & S_IXUSR) else 'S'
    if mode & S_ISGID:
        bits[6] = 's' if (mode & S_IXGRP) else 'l'
    if mode & S_ISVTX:
        bits[9] = 't' if (mode & S_IXOTH) else'T'

    bits = [i for i in bits if i != 0]
    return ''.join(bits)


def get_filename_ext(filename: str) -> str:
    return Path(filename).suffix


if __name__ == "__main__":
    pathname = "hello.txt"

    argc = len(sys.argv)

    file_ext = get_filename_ext(pathname)
    print(f"file ext: {file_ext}")

    buf = os.stat(pathname)
    mode = buf.st_mode
    size = buf.st_size

    perms = ls_perms(mode)
    print(perms)

    pw = pwd.getpwuid(buf.st_uid)
    print(f"name: {pw.pw_name}")

    gr = grp.getgrgid(buf.st_gid)
    print(f"group: {gr.gr_name}\n")

    for filename in os.listdir("."):
        print(f"filenames: {filename}")
