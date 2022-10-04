import jinja2
import yaml

CONFIG_PATH = 'config.yaml'
TEMPLATES_PATH = 'templates'

with open(CONFIG_PATH) as config_file_handle:
    config = yaml.safe_load(config_file_handle)

# Load jinja: 
jinja_loader = jinja2.FileSystemLoader(searchpath=TEMPLATES_PATH)
jinja = jinja2.Environment(loader=jinja_loader)
template = jinja.get_template(f"resume.html.j2")
result = template.render(**config)

print(result)