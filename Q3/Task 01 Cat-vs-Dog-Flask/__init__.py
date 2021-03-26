import os
import secrets
from PIL import Image
from flask import Flask, render_template, url_for, request
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'


class PictureForm(FlaskForm):
    picture = FileField('Upload Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = PictureForm()

    image_file = url_for('static', filename='sample_image.jpg')
    animal = 'Dog'

    if request.method == 'POST':
        if form.validate_on_submit():
            if form.picture.data:
                random_hex = secrets.token_hex(8)
                _, f_ext = os.path.splitext(form.picture.data.filename)
                picture_fn = random_hex + f_ext
                picture_path = os.path.join(app.root_path, 'static\\cache', picture_fn)
                i = Image.open(form.picture.data)
                i.save(picture_path)

                image_file = url_for('static', filename='cache/'+picture_fn)
                animal = predict(picture_path)

    return render_template('index.html', image_file=image_file, form=form, animal=animal)


# A method to predict the image as a cat or dog
def predict(path):
    # Now Judge as a Cat or Dog
    # make a prediction for a new image.
    from tensorflow.keras.preprocessing.image import load_img
    from tensorflow.keras.preprocessing.image import img_to_array
    # load and prepare the image
    # load the image
    img = load_img(path, target_size=(50, 50))
    # convert to array
    img = img_to_array(img)
    # reshape into a single sample with 3 channels
    img = img.reshape(1, 50, 50, 3)
    # center pixel data
    img = img.astype('float32')
    img = img - [123.68, 116.779, 103.939]
    # predict the class
    from tensorflow.keras.models import load_model
    # Getting model path
    model_path = os.path.join(app.root_path, 'static\\dog-vs-cat.h5')
    # loading model
    model = load_model(model_path)
    # Predicting Result
    result = model.predict(img)
    # Return Cat or Dog
    return 'Dog' if result else 'Cat'


if __name__ == '__main__':
    app.run()
