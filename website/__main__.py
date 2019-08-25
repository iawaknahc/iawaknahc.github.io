import os
import os.path
import yaml

from jinja2 import Environment, FileSystemLoader


def main():
    template_dir = "website/templates/"
    env = Environment(
        loader=FileSystemLoader(template_dir),
        autoescape=True,
        trim_blocks=True,
        lstrip_blocks=True,
    )
    for root, _, filenames in os.walk(template_dir):
        for filename in filenames:
            no_ext, ext = os.path.splitext(filename)
            if filename[0:1] == "_" or ext != ".html":
                continue

            template_name = os.path.join(root, filename)[len(template_dir):]
            template = env.get_template(template_name)

            try:
                with open(os.path.join(root, f"{no_ext}.yaml")) as f:
                    context = yaml.safe_load(f)
            except OSError:
                context = {}

            with open(template_name, "w") as f:
                f.write(template.render(context))


if __name__ == "__main__":
    main()
