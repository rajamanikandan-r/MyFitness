from flask import Flask
import requests as req

app = Flask(__name__)

@app.route("/")
def index():
	headers = {"Authorization" : "Bearer ya29.a0AfB_byAmxBdHPcPzTxA3bONUlKP2hhTopJtDElMAQVvCmN7SJ7MxMzEAc3LgzGxjsqYnTPi5iZaS8nJvJZZBmsmLYmYdEEkmQeXE6kVaVToqmt2quB3WxO0NvELIkDkTnMCSmHOqSPuiLz_mvJ4s81nqRE0E_bC9iqc5aCgYKAdcSARMSFQHGX2Mi95BTokhy1OGpf-cNsMdVCw0171"}
	params = {"ActivityType" : 8 }
	response = req.get("https://www.googleapis.com/fitness/v1/users/me/sessions", headers = headers, params = params)

	return response.text