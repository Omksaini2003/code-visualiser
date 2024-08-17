import re
import json

def parse_cpp_code(code: str):
    # Regex pattern for matching function definitions
    function_pattern = re.compile(r'(?![a-z])[^\:,>,\.]([a-zA-Z_]\w*)\s*\(')
    if_pattern = re.compile(r'\bif\s*\(.*\)\s*{')
    else_if_pattern = re.compile(r'\belse\s+if\s*\(.*\)\s*{')
    else_pattern = re.compile(r'\belse\s*{')
    while_pattern = re.compile(r'\bwhile\s*\(.*\)\s*{')
    for_pattern = re.compile(r'\bfor\s*\(.*\)\s*{')

    def parse_block(code_lines, start_index=0):
        structure = []
        i = start_index
        while i < len(code_lines):
            line = code_lines[i].strip()
            if if_pattern.match(line):
                block, i = parse_block(code_lines, i + 1)
                structure.append({"if": block})
            elif else_if_pattern.match(line):
                block, i = parse_block(code_lines, i + 1)
                structure.append({"elseif": block})
            elif else_pattern.match(line):
                block, i = parse_block(code_lines, i + 1)
                structure.append({"else": block})
            elif while_pattern.match(line):
                block, i = parse_block(code_lines, i + 1)
                structure.append({"while": block})
            elif for_pattern.match(line):
                block, i = parse_block(code_lines, i + 1)
                structure.append({"for": block})
            elif line == "}":
                return structure, i
            i += 1
        return structure, i

    def parse_functions(code_lines):
        structure = {}
        i = 0
        while i < len(code_lines):
            line = code_lines[i].strip()
            matches = list(re.finditer(function_pattern, line))
            if matches:
                func_name = matches[-1].group(1)
                block, i = parse_block(code_lines, i + 1)
                structure[func_name] = block
            else:
                i += 1
        return structure

    # Split the code into lines and parse it
    code_lines = code.splitlines()
    parsed_structure = parse_functions(code_lines)

    return parsed_structure






# Read the code from file and parse it
filename = './sample.cpp'

with open(filename, 'r') as file:
    code = file.read()

parsed_json = parse_cpp_code(code)






# Export JSON to file
output_filename = './parsed_structure.json'
with open(output_filename, 'w') as json_file:
    json.dump(parsed_json, json_file, indent=4)
