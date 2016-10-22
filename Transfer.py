from flask import Flask, request, redirect, url_for, send_from_directory
from werkzeug import secure_filename
from TopicManager import TopicManager
from Topic import Topic
import os


UPLOAD_FOLDER = './uploads'
# ALLOWED_EXTENSIONS = set(['mp3', 'wav'])
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
topicManager = TopicManager()


@app.route('/')
def welcome():
    return 'welcome!'


@app.route('/addtopic', methods=['GET', 'POST'])
def addTopic():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            title = request.form['title']
            genere = request.form['genere']
            script = request.form['script']
            path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

            topic = topicManager.addTopic(title, genere, path, script)
            topicManager.analyseTopic(topic)
            # return redirect(url_for('getTopicFile', filename=filename))
            # return redirect(url_for('getTopic', id=topic.id))

            return str(topic.sttResult)

    return '''
    <!doctype html>
    <title>Upload Topic</title>
    <h1>Upload Topic</h1>
    <form action="" method=post enctype=multipart/form-data>
        <p>Title: <input type=text name=title>
        <p>Genere: <input type=text name=genere>
        <p>Script: <input type=text name=script>
        <p><input type=file name=file>
            <input type=submit value=Upload>
    </form>
    '''


@app.route('/gettopicfile/<filename>')
def getTopicFile(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


# @app.route('/gettopic/<id>')
# def getTopic(id):
#     topic = topicManager.getTopic(id)
#     result = 'Title : ' + str(topic.title) + '<br>Genere : ' + str(topic.genere) + \
#         '<br>Script : ' + str(topic.script) + '<br><br><b>STT Result</b> : '
#     sentences = ''
#     print topic.sttResult
#     if topic.sttResult:
#         for sentence in topic.sttResult:
#             sentences += sentence[0] + '<br>'
#             sentences += str(sentence[1]) + '<br>'
#         result += sentences
#     return result

mSTT = ""
@app.route('/gettopic/<id>')
def getTopic(id):
    global mSTT
    topic = topicManager.getTopic(id)
    if mSTT == "":
        topicManager.analyseTopic(topic)
        mSTT = topic.sttResult;
    topic.sttResult = mSTT
    result = str(topic.id) + '\r\n' + str(topic.title) + '\r\n' + str(topic.genere) + \
        '\r\n' + str(topic.script) + '\r\n' + str(topic.mediaFilePath) + '\r\n'
    if topic.sttResult:
        for sentence in topic.sttResult:
            result += sentence[0] + '\r\n'
            result += str(sentence[1]) + '\r\n'
    print result
    return result
# TODO


@app.route('/gettopics')
def gettopics():
    result = ''
    topics = topicManager.getAllTopics()
    for topic in topics:
        result += str(topic.id) + '\r\n' + str(topic.title) + '\r\n'

    return result


if __name__ == '__main__':
    app.run(host='0.0.0.0')
    # app.run()
