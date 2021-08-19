# python_to_dot_proto_file
Given an instantiated python class or dictionary, generates the corresponding .proto file

# Purpose
The purpose of this project is to give people experimenting with protocol buffers in python a basic understanding of their structure and how to create them.  With nothing more than an instantiated class or dictionary, the user can get an example of what a protocol buffer would look like if they were to write it for their classes/dicts.

# Basic Usage
import the python_object_to_proto file

use the convert_objs_to_proto function to generate the proto file

filename defaults to POTP.proto, but can be manually set

example of function usage

convert_objs_to_proto([instantiatedClass1, instantiatedClass2, dict1, dict2], packageName="MyPackage", filename="myProtoFile.proto"):

for an example of a class and dict to use, see [Test_Classes.py]

# Protobuf and Protoc Usage
If you want to compile the generated proto file (if this doesn't make sense to you work through the guide in additional resources), the command is:

protoc -I=<SRC_DIR> --python_out=<DST_DIR> <SRC_DIR>/<filename>.proto

protoc -I="./" --python_out="./" ./<filename>.proto

# Limitations
This program has some major limitations and does not encompass the full scope and power of protocol buffers. First off, Python does not have typing and that makes things challenging. This program is limited by what it can guess based on an instantiated instance of a python class or dictionary. There is a lot it cannot guess from an instance, but it provides a solid starting point for users to add modify and expand upon the generated file.

Here are some things I recommend the user experiment with once they have generated a basic template:
* The "optional" and "required" qualifiers
* Enumerations using the keyword "enum"
* Datatypes that were not able to be expressed with python such as int64, unsigned ints, and other int variantes

# Where To Go From Here
It may be worth looking further into whether enumerations are possible to generate. A cursorary look suggested it wouldn't be possible, but I may be wrong.

# Additional Resources

General guide - developers.google.com/protocol-buffers/ 

Python specific guide - developers.google.com/protocol-buffers/docs/pythontutorial

Proto3 and Types - https://developers.google.com/protocol-buffers/docs/proto3