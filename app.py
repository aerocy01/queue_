from queue_class import Flask, render_template, request, redirect, url_for
from queue import Queue

app = Flask(__name__)

q = Queue()

@app.route('/')
def index():
    """Display the queue and provide options to enqueue/dequeue"""
    return render_template('index.html', queue=q)

@app.route('/enqueue', methods=['POST'])
def enqueue():
    """Add an item to the queue"""
    item = request.form.get('item')
    if item:
        q.enqueue(item)
    return redirect(url_for('index'))

@app.route('/dequeue')
def dequeue():
    """Remove an item from the queue"""
    q.dequeue()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)