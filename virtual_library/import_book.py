import yaml

with open('fixtures.yaml', 'r') as file:
    content=yaml.safe_load_all(file)
    print(content)

