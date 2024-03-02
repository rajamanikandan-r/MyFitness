Testing if heroku deploy works

Setting up

Mac/Linux
python -m venv .venv
. .venv/bin/activate

pip install flask
flask --app flaskr init-db
flask --app flaskr run --debug

curl -X POST -H "Content-Type: application/json" -d '{"name": "short", "duration" : 34, "distance" : 12, "calories" : 123, "averageHR" : 178, "type" : 0 }' http://127.0.0.1:5000/create

