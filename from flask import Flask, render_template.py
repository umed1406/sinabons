from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    # Получаем список всех файлов изображений в папке static/images
    image_folder = os.path.join('static', 'images')
    images = [f for f in os.listdir(image_folder) if f.startswith('img') and f.endswith('.jpg')]
    images.sort(key=lambda x: int(x[3:-4]))  # Сортировка по номеру изображения
    return render_template('index.html', images=images)

if __name__ == '__main__':
    app.run(debug=True)
    