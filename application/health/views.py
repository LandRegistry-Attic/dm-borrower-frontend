from flask import Blueprint, render_template

health = Blueprint('health', __name__,
                   template_folder='/templates',
                   static_folder='static')


@health.route('/')
def health_main():
    return render_template('health.html')
