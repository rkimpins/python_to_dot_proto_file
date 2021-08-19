from Test_Classes import TestClass
from Test_Classes import TestDict


PROTOBUF_COUNTER = 0


def protobuf_string_type_of(var):
	if isinstance(var, str):
		return "string"
	elif isinstance(var, int):
		return "int32"
	elif isinstance(var, float):
		return "float"
	elif isinstance(var, bool):
		return "bool"
	elif isinstance(var, bytes):
		return "bytes"
	elif isinstance(var, list):
		return "repeated " + protobuf_string_type_of(var[0])
	else:
		return "unknown"
	#enum?


def add_dict_to_proto(obj, dict_name, proto, tab_level=0):
	global PROTOBUF_COUNTER
	proto += "\n" + "\t" * tab_level + f"message {dict_name} = " + "{"

	for key, val in obj.items():
		proto += "\n" + "\t" * (tab_level + 1) + f"{key} {protobuf_string_type_of(val)} = {PROTOBUF_COUNTER}"
		PROTOBUF_COUNTER += 1
	proto += "\n" + "\t" * tab_level + "}"
	return proto


def add_class_to_proto(obj, proto, tab_level=0):
	global PROTOBUF_COUNTER
	proto += "\t" * tab_level + f"message {type(obj).__name__} " + "{"
	for attr, value in obj.__dict__.items():
		if isinstance(value, (dict)):
			proto = add_dict_to_proto(value, attr, proto, tab_level = tab_level + 1)
			#proto += "\n" + "\t" * (tab_level + 1) + "REPEATED"
		else:
			proto += "\n" + "\t" * (tab_level + 1) + f"{protobuf_string_type_of(value)} {attr} = {PROTOBUF_COUNTER};"
			PROTOBUF_COUNTER += 1
	proto += "\n" + "\t" * tab_level + "}"
	return proto


def convert_objs_to_proto(obj_list, syntax="proto3", packageName="temporaryName", tab_level=0, filename="POTP.proto"):
	proto = "\\*This proto file was generated using the Python Object To Proto utility created by (rkimpins)*/"
	proto += "\n" + "\t" * tab_level +  f"syntax = \"{syntax}\";"
	proto += "\n\n" + "\t" * tab_level + f"package {packageName};"
	proto += "\n\n"
	for obj in obj_list:
		if isinstance(obj, dict):
			proto = add_dict_to_proto(obj, "Dict", proto)
		else:
			proto = add_class_to_proto(obj, proto)
		proto += "\n"

	write_to_file(proto, filename)
	print(proto)
	return proto

def write_to_file(proto, file_name):
	with open(file_name, "w") as f:
		f.write(proto)


def main():
	convert_objs_to_proto([TestClass(), TestDict])

if __name__ == "__main__":
	main()