import jinja2
import yaml

CONFIG_PATH = 'config.yaml'
TEMPLATES_PATH = 'templates'
RESUME_TEMPLATE_PATH = 'resume.html.j2'

# Load config: 
with open(CONFIG_PATH) as config_file_handle:
    config = yaml.safe_load(config_file_handle)

# Render template: 
jinja_loader = jinja2.FileSystemLoader(searchpath=TEMPLATES_PATH)
jinja = jinja2.Environment(loader=jinja_loader)
template = jinja.get_template(RESUME_TEMPLATE_PATH)
result = template.render(**config)

# Dump html: 
print(result)
