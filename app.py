from flask import Flask, render_template, request, redirect
from qiskit import *
from qiskit.tools.visualization import plot_histogram
from qiskit.tools.visualization import plot_state_qsphere
from dj import runDJ
from quantum_teleportation import q_teleportation

app = Flask(__name__)

# global_vars = {}

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')

@app.route('/teleportation', methods=['POST', 'GET'])
def teleportation():
    
    ckt, fig, time = q_teleportation()
    
    # histogram
    simulator = Aer.get_backend('qasm_simulator')
    result = execute(ckt, backend=simulator, shots=1024).result()
    counts = result.get_counts()
    histo = plot_histogram(counts)
    histo.savefig('./static/images/hist.png')
    
    # qsphere
    sim2 = Aer.get_backend('statevector_simulator')
    result2 = execute(ckt, backend=sim2, shots=1024).result()
    state_v = result2.get_statevector(ckt)
    qsph = plot_state_qsphere(state_v)
    qsph.savefig('./static/images/qsph.png')

    return render_template('quantum_teleportation.html', time=time)


@app.route('/deutsch-jozsa', methods=['POST', 'GET'])
def deutsch_jozsa():
    if(request.method == 'POST'):
        type = request.form['option']
        n = int(request.form['n'])
        hist, fig, time = runDJ(type, n)
        fig.savefig('./static/images/dj-ckt.png')
        hist.savefig('./static/images/dj-hist.png')
        return render_template('/dj.html', type=type, n=n, time=time)
    else:
        return render_template('dj.html')


if __name__ == '__main__':
    app.run(debug=True)
