from flask import Flask, render_template

app = Flask(__name__)

@app.route('/dash')
def display_dashboard():
    # Paste the copied iframe code here
    #grafana_iframe = '<paste your iframe code here>'
    #return render_template('dashboard.html', grafana_iframe=grafana_iframe)

    dummy_iframe_code = '<iframe width="800" height="600" src="https://www.example.com" frameborder="0" allowfullscreen></iframe>'
    return render_template('dashboard.html', grafana_iframe=dummy_iframe_code)


    
if __name__ == '__main__':
    app.run(debug=True)