"""Quick test runner for Exercise 1.1

Runs a small test against the add.add function.
"""
import importlib.util
import sys
from pathlib import Path


def load_module_from_path(path: str, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    repo_root = Path(__file__).resolve().parent
    add_py = repo_root / "add.py"
    mod = load_module_from_path(str(add_py), "add_module")

    assert hasattr(mod, "add"), "add.py must define add(a, b)"
    assert mod.add(2, 3) == 5, "add(2,3) should equal 5"
    assert mod.add(-1, 1) == 0, "add(-1,1) should equal 0"
    print("All tests passed.")


if __name__ == "__main__":
    main()
