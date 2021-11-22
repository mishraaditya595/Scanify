from flask import *
import os, pytesseract
from flask_uploads import *
from PIL import Image

project_dir = os.path.dirname(os.path.abspath("__file__"))

app = Flask(__name__, static_url_path = '', static_folder = 'static', template_folder = 'templates')

photos = UploadSet('photos', IMAGES)

app.config['DEBUG'] = True
app.config['UPLOAD_FOLDER'] = "/home/aditya/Projects/Scanify/OCR/images"

class GetText(object):
      def __init__(self, file):
          self.file = pytesseract.image_to_string(Image.open(project_dir + '/images/' + file))
          
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
         if 'photo' not in request.files:
             return 'there is no photo in the form'
         name = request.form['img-name']+'.jpg'
         photo = request.files['photo']
         path = os.path.join(app.config['UPLOAD_FOLDER'], name)
         photo.save(path)
         
         textObject = GetText(name)
         print('TEXT OBJECT' + textObject.file)
         
         return textObject.file
         
    return render_template('index.html')  
    
#@app.route("/api/upload",methods=['POST'])
#def upload
    
if __name__ == "__main__":
    app.run()
