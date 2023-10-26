from flask import Flask, render_template, request
import csv

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    image = request.files['image']
    image.save('uploads/' + image.filename)

    # Gửi thông tin tên ảnh và thời gian vào file CSV
    with open('D:\pycharmProject\warningbox\log.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([image.filename, request.form['timestamp']])

    return 'Upload successful!'


@app.route('/alerts')
def alerts():
    # Đọc dữ liệu từ file CSV và truyền nó vào template để hiển thị
    data = []
    with open('D:\pycharmProject\warningbox\log.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)

    return render_template('alerts.html', data=data)


if __name__ == '__main__':
    app.run()
