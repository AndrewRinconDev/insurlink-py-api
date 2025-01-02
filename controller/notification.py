from flask import request, jsonify, Blueprint
from models.response.response import Response
from services.notification import sendEmailNotification

notification_bp = Blueprint('notification', __name__, url_prefix='/notification')

@notification_bp.route('/', methods=['POST', 'GET'])
def saveEmailNotification():
  try:
    if request.method == 'POST':
      notificationData = request.get_json()
      responseData = sendEmailNotification(notificationData)
      response = Response(statusCode=200, hasError=False, message="Success", data=responseData)
      return jsonify(response.dict()), 200  
    else:
      return jsonify(Response(statusCode=404, hasError=True, message="Upload API GET Request Running").dict()), 404
  except Exception as e:
    print('Error', e)
    return jsonify(Response(statusCode=500, hasError=True, message=str(e))), 500