import xml.etree.ElementTree as ET
import argparse
import os
from functools import reduce

parser = argparse.ArgumentParser(description='Sync fuji raw studio settings')
parser.add_argument('-p', '--images-path', help='Path to the folder containing your files')

args = parser.parse_args()

extensions = ['FP2', 'FP3']

def match_extension(f):
  for e in extensions:
    if f.endswith(e):
      return True
  return False

def parse_file(fname):
  return (fname, ET.parse(fname))

def manipulate_xml(tree):
  root = tree.getroot()
  root.find('PropertyGroup').find('ImageSize').text = 'M3x2'
  root.find('PropertyGroup').find('ImageQuality').text = 'Normal'
  root.find('PropertyGroup').find('GrainEffect').text = 'OFF'
  return tree

files = filter(match_extension, os.listdir(args.images_path))

parsed = map(lambda filename: parse_file(args.images_path + '/' + filename), files)
manipulated = map(lambda x: (x[0], manipulate_xml(x[1])), parsed)

file = next(manipulated)

def persist_file(file):
  path = file[0] + '2'
  print('Writing to path ' + path)
  file[1].write(file[0], encoding='utf-8', xml_declaration=True)


print('Manipulating xmls')

for f in manipulated:
  persist_file(f)

print('Done')


# print(ET.tostring(file[1].getroot(), encoding='utf8', method='xml'))

# print([f for f in files])
