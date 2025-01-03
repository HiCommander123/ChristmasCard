from flask import render_template, request, redirect, url_for
from flask import flash, redirect, url_for, render_template, request
from app import app, db
from app.models import Letter
from werkzeug.utils import secure_filename
import os

@app.route('/')
def index():
    query = request.args.get('query')
    if query:
        letters = Letter.query.filter(
            (Letter.author.ilike(f'%{query}%')) | 
            (Letter.content.ilike(f'%{query}%'))
        ).all()
    else:
        letters = Letter.query.all()
    return render_template('index.html', letters=letters)

@app.route('/write', methods=['GET', 'POST'])
def write_letter():
    if request.method == 'POST':
        author = request.form['author']
        content = request.form['content']
        image = request.files['image']
        
        if image:
            filename = secure_filename(image.filename)
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        else:
            filename = None
        
        letter = Letter(author=author, content=content, image=filename)
        db.session.add(letter)
        db.session.commit()
        return redirect(url_for('index'))
    
    return render_template('write_letter.html')

@app.route('/letter/<int:letter_id>')
def view_letter(letter_id):
    letter = Letter.query.get_or_404(letter_id)
    return render_template('view_letter.html', letter=letter)

@app.route('/delete_letter/<int:letter_id>', methods=['POST'])
def delete_letter(letter_id):
    letter = Letter.query.get_or_404(letter_id)
    
    # 이미지 파일 삭제 (선택사항)
    if letter.image:
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], letter.image)
        if os.path.exists(image_path):
            os.remove(image_path)
    
    # 데이터베이스에서 편지 삭제
    db.session.delete(letter)
    db.session.commit()
    
    return redirect(url_for('index'))

from flask import redirect, url_for, request

@app.route('/edit_letter/<int:letter_id>', methods=['GET', 'POST'])
def edit_letter(letter_id):
    letter = Letter.query.get_or_404(letter_id)
    if request.method == 'POST':
        letter.author = request.form['author']
        letter.content = request.form['content']
        db.session.commit()
        flash('편지가 성공적으로 수정되었습니다.', 'success')
        return redirect(url_for('view_letter', letter_id=letter.id))
    return render_template('edit_letter.html', letter=letter)

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    user_ip = request.remote_addr
    return render_template('index.html', user_ip=user_ip)
