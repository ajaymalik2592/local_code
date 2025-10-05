import os

# Define hierarchy
structure = {
    "Artificial_Intelligence": {
        "Machine_Learning": {
            "Supervised_Learning": {},
            "Unsupervised_Learning": {},
            "Reinforcement_Learning": {}
        },
        "Deep_Learning": {
            "CNNs": {},
            "RNNs": {},
            "Transformers": {}
        }
    }
}

def create_module(base_path, structure):
    for module_name, submodules in structure.items():
        module_path = os.path.join(base_path, module_name)
        os.makedirs(module_path, exist_ok=True)

        # Add __init__.py to make it a Python package
        init_file = os.path.join(module_path, "__init__.py")
        if not os.path.exists(init_file):
            with open(init_file, "w") as f:
                f.write(f"# {module_name} module\n")
            print(f"📦 Created Python module: {init_file}")

        # Recurse into submodules
        create_module(module_path, submodules)

if __name__ == "__main__":
    base_dir = "./AI_Hierarchy_Modules"
    os.makedirs(base_dir, exist_ok=True)
    create_module(base_dir, structure)
    print("\n✅ Python module hierarchy created successfully!")
