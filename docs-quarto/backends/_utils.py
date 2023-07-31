from jinja2 import Environment, FileSystemLoader, select_autoescape
from quartodoc import Auto, blueprint, MdRenderer

def badges(imports, exports):
    context = {**locals()}

    env = Environment(
        loader=FileSystemLoader("."),
        autoescape=select_autoescape()
    )

    template = env.get_template("badges.md.j2")

    return template.render(**context)


def render_doc(object_path, header_level, members = []):
    auto = Auto(name=object_path, members = members)
    bp = blueprint(auto)
    return MdRenderer(header_level = header_level).render(bp)



def default_template(
    backend_name,
    backend_url,
    intro,
    backend_module,
    backend_param_style,
    is_experimental = None,
    version_added = None,
    development_only = None,
    is_core = None,
    mgr = None,
    do_connect_base = None,
    exclude_backend_api = None,
    ):

    context = {**locals()}

    env = Environment(
        loader=FileSystemLoader("."),
        autoescape=select_autoescape()
    )

    template = env.get_template("template.md.j2")

    return template.render(**context, render_doc = render_doc)
