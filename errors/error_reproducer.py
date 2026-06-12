import os

print("--- pydisasm output ---")

os.system("pydisasm test_4.pyc")

print()

print("--- xdis.std.get_instructions output ---")
import xdis.std as dis
from xdis.disasm import load_module

mod = load_module("test_4.pyc")

co = mod[3]

for instr in dis.get_instructions(co):
    print(instr.opname, instr.arg if instr.arg is not None else 0)

print()
