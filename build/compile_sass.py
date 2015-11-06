from os import path
import sass as libsass

__dot = path.dirname(path.realpath(__file__))
__toolkit_dir = path.join(__dot, 'elements/govuk_template/')
__elemets_dir = path.join(__dot, 'elements/')
__output_dir = path.join(__dot, '../app/static/elements/')


def __compile_sass(_in, out, **kw):
    css = libsass.compile(
        string=_in.read(),
        include_paths=[__toolkit_dir, __elemets_dir]
    )
    out.write(css)


def compile_sass():
    __compile_sass(open(__elemets_dir + 'main.scss', 'r'), open(__output_dir + 'main.css', 'w+'))
