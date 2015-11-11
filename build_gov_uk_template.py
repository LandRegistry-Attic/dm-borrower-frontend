# This will rebuild the gov_uk_template directories from the
# latest available in https://github.com/alphagov/govuk_template
# WARNING:
# Overwrites the files in app/static/govuk_template
# Overwrites the files in app/views/jinja
from build.tap import download_jinja
from build.compile_sass import compile_sass

download_jinja()
compile_sass()
