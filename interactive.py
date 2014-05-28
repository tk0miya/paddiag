import json
from utils import decode_source
from flask import Flask, request, render_template, make_response

app = Flask(__name__)


@app.route('/')
def flowchartdiag_form():
    return render_template('index.html')


@app.route('/image', methods=['GET', 'POST'])
def flowchartdiag_image():
    if request.method == 'POST':
        source = request.form['src']
    else:
        source = request.args.get('src')

    encoding = request.args.get('encoding')
    compression = request.args.get('compression')

    source = decode_source(source, encoding, compression)

    format = request.args.get('format', 'SVG')
    image = flowchartdiag_generate_image(source, format)
    if encoding == 'jsonp':
        callback = request.args.get('callback')
        if callback:
            dumped = json.dumps(image, ensure_ascii=False)
            jsonp = u'%s(%s)' % (callback, dumped)
        else:
            jsonp = ''

        response = make_response(jsonp)
        response.headers['Content-Type'] = 'text/javascript'
    else:
        response = make_response(image['image'])
        if format == 'PNG':
            response.headers['Content-Type'] = 'image/png'
        elif encoding == 'base64':
            response.headers['Content-Type'] = 'image/svg+xml'
        else:
            response.headers['Content-Type'] = 'text/plain'

    return response


def flowchartdiag_generate_image(source, format):
    from blockdiag import parser, builder, drawer
    from blockdiag.utils.fontmap import FontMap
    from StringIO import StringIO
    from make_flowchart import parse, write_stmt

    try:
        ast = parse(source)
        dot = StringIO()
        dot.write("{\n")
        dot.write("  orientation = portrait\n")
        dot.write("  edge_layout = flowchart\n")
        dot.write("  node_width = 256\n")
        write_stmt(dot, ast.body)
        dot.write("}\n")

        tree = parser.parse_string(dot.getvalue())
        diagram = builder.ScreenNodeBuilder.build(tree)
        draw = drawer.DiagramDraw(format, diagram, fontmap=FontMap(),
                                  ignore_pil=True)
        draw.draw()

        image = draw.save()
        etype = None
        error = None
    except Exception, e:
        image = ''
        etype = e.__class__.__name__
        error = str(e)

    return dict(image=image, etype=etype, error=error)


if __name__ == '__main__':
    app.run()
