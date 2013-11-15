from re import search, sub

from django import template


register = template.Library()


class TrimlinesNode (template.Node):
    def __init__ (self, begin_lines, minimum_empty_lines, end_lines, nodelist):
        self.begin_lines         = begin_lines
        self.minimum_empty_lines = minimum_empty_lines
        self.end_lines           = end_lines
        self.nodelist            = nodelist

    def render (self, context):
        output = self.nodelist.render(context)

        # trim trailing whitespace
        output = sub(r'[ \t]+\n', '\n', output)
        output = sub(r'[ \t]+$',  '',   output)

        # set mid empty lines
        output = sub(
            '\n{{{},}}'.format(self.minimum_empty_lines),
            '\n' * self.minimum_empty_lines,
            output
        )

        # set beginning lines
        if self.begin_lines == 0:
            output = sub(r'^[ \t\n]*', '', output)
        else:
            pattern = r'^([ \t]*)\n*'
            match = search(pattern, output)
            output = sub(pattern, match.group(1) + '\n' * self.begin_lines, output)

        # set end lines
        output = sub(r'\n*$', '\n' * self.end_lines, output)

        return output


@register.tag()
def trimlines (parser, token):
    try:
        contents = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError("{} tag has 0 to 3 arguments".format(token.contents.split()[0]))

    if len(contents) == 1:
        begin_lines         = 0
        minimum_empty_lines = 1
        end_lines           = 0
    elif len(contents) == 2:
        begin_lines         = 0
        minimum_empty_lines = int(contents[1])
        end_lines           = 0
    elif len(contents) == 3:
        begin_lines         = int(contents[1])
        minimum_empty_lines = int(contents[2])
        end_lines           = 0
    elif len(contents) == 4:
        begin_lines         = int(contents[1])
        minimum_empty_lines = int(contents[2])
        end_lines           = int(contents[3])
    else:
        raise template.TemplateSyntaxError("{} tag has 0 to 3 arguments".format(contents[0]))

    nodelist = parser.parse(('endtrimlines',))
    parser.delete_first_token()
    return TrimlinesNode(begin_lines, minimum_empty_lines, end_lines, nodelist)
