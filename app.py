from flask import Flask, render_template
import content

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', feature_data=content.feature)

@app.route('/about-us')
def about():
    return 'this is home route'
@app.route('/product')
def product():
    return render_template('all_product.html')

@app.route('/product/<value>')
def product_inner(value):
    if value== 'mattress':
        return render_template('product.html',product_det=content.product_mat)
    elif value == 'pillow':
        return render_template ('pillow.html',product_det=content.product_pillow)
    elif value == 'protector':
        return render_template ('Protector.html',product_det=content.product_protecor)

@app.route('/product/<value>/<value1>')
def product_det(value,value1):
    if value == "mattress":
        for i in content.product_mat:
            if i["name"] == value1 :
                data = {'name':i['name'],'dics':i['dics'],'images':i['images']}
                size=i['size']
    return render_template ('pro_det.html',data=data,size=size)

@app.route('/product/<value>/<value1>/<value2>')
def product_det_size(value,value1,value2):
    if value == "mattress":
        value2=(int(value2)-1)
        for i in content.product_mat:
            if i["name"] == value1 :
                data = {'name':i['name'],'dics':i['dics'],'size':i['size'][value2],'images':i['images']}
                size=i['size']
    return render_template ('pro_det.html',data=data,size=size)

@app.route('/terms_and_condition')
def tc():
    return render_template ('tc.html')
    
if __name__ == '__main__':
    app.run(debug=True)
