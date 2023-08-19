from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/api/upload_data/',methods=['POST'])
def api():
    md5_hash = request.form.get('file_md5_hash')
    md5_hash = request.form.get('file_size')
    print(md5_hash)
    return "Yes"
app.run(debug = True)