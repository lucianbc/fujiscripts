import os
import itertools

RAWS_ROOT = '/Volumes/samba/usb1_1/Photography/'
PHOTOS_ROOT = '/Volumes/samba/usb1_1/Photos/'

# walker = os.walk(RAWS_ROOT)

# print(next(walker))
# print(next(walker))
# print(next(walker))
# print(next(walker))
# print(next(walker))

# print("======================")

# def day_paths(root):
#   dirs = sorted(os.listdir(root))
#   for d in dirs:
#     print(d)
  
# print(day_paths(RAWS_ROOT))


def day_albums(root):
  for level1 in folders_in(root):
    for level2 in folders_in(os.path.join(root, level1)):
      for level3 in folders_in(os.path.join(root, level1, level2)):
        yield os.path.join(level1, level2, level3)


def folders_in(path):
  return filter(lambda x: os.path.isdir(os.path.join(path, x)), os.listdir(path))


def folder_is_empty(root, path):
  return len(os.listdir(os.path.join(root, path))) == 0


def photos_not_edited():
  print("Indexing raws")
  raws_days = { r for r in day_albums(RAWS_ROOT) }
  print("Finished indexing raws")
  print("Indexing photos")
  photos_days = { r for r in day_albums(PHOTOS_ROOT) }  
  print("Finished indexing photos")
  not_in_photos = (p for p in raws_days if p not in photos_days)
  empty_photos = (p for p in photos_days if folder_is_empty(PHOTOS_ROOT, p))
  not_edited = sorted(itertools.chain(not_in_photos, empty_photos))
  print("Your unedited days are:")
  for x in not_edited:
    print(x)


# for x in sorted(day_albums(RAWS_ROOT)):
#   print(x)

# for x in sorted(day_albums(PHOTOS_ROOOT)):
#   print(x)


photos_not_edited()
# print(day_albums(RAWS_ROOT))
