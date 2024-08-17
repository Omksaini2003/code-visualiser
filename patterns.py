import re

# Regex pattern for matching function definitions

function_pattern = re.compile(r'(?![a-z])[^\:,>,\.]([a-zA-Z_]\w*)\s*\(')
if_pattern = re.compile(r'\bif\s*\(.*\)\s*{')
else_if_pattern = re.compile(r'\belse\s+if\s*\(.*\)\s*{')
else_pattern = re.compile(r'\belse\s*{')
while_pattern = re.compile(r'\bwhile\s*\(.*\)\s*{')
for_pattern = re.compile(r'\bfor\s*\(.*\)\s*{')
