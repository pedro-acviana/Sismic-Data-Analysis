# Configuration file for voila.

c = get_config()

# Template configuration
c.Voila.template = 'material'

# Enable widget extensions
c.VoilaConfiguration.enable_nbextensions = True

# File extension to use for generated files
c.VoilaConfiguration.file_extension = '.html'

# Strip source code from rendered notebook
c.VoilaConfiguration.strip_sources = True

# Show tracebacks in rendered notebooks
c.VoilaConfiguration.show_tracebacks = True

# Output directory for static files
c.Voila.static_root = 'static'

# Tornado settings
c.Voila.tornado_settings = {
    'allow_origin': '*',
    'allow_methods': 'GET,POST,PUT,DELETE,OPTIONS',
    'allow_headers': 'Origin,Accept,Content-Type,X-Requested-With,X-CSRF-Token',
}
