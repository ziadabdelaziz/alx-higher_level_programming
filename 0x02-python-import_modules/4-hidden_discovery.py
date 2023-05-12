#!/usr/bin/pyton3
if __name__ == "__main__":
    import importlib
    module = importlib.import_module("hidden_4")
    names = dir(module)
    
    for name in sorted(names):
        if name.startswith("__"):
            continue
        print(name)
