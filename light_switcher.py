from flask import Flask, request
from flask_restx import Api, Resource, fields
import pigpio, time

status = None

pi = pigpio.pi()

app = Flask(__name__)
api = Api(app, version="1.0", title="LightSwitcher API Document", description="LightSwitcher is an API server that controls DC serbo motors connected to a RaspberryPi", doc="/doc/", default="Default Endpoint", default_label="default")

response_model = api.model("LightSwitcherResponse", {
    "status": fields.String(description="Status of light")
})
expect_model = api.model("LightSwitcherExpect", {
    "param": fields.String(description="Parameter for switching light")
})

@api.route("/")
@api.expect(expect_model)
class Switch(Resource):
    @api.marshal_with(response_model)
    def post(self):
        if request.json["param"] == "ON":
            pi.set_servo_pulsewidth(18, 1150)
            time.sleep(0.25)
            pi.set_servo_pulsewidth(18, 1500)
            status = 1
            print(status)
            return {"status": str(status)}
        elif request.json["param"] == "OFF":
            pi.set_servo_pulsewidth(19, 1500)
            time.sleep(0.25)
            pi.set_servo_pulsewidth(19, 1150)
            status = 0
            print(status)
            return {"status": str(status)}

        print("Error")
        return {"status": str(-1)}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=False)

