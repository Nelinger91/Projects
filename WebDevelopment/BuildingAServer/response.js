response = {
    resToString: function(resObj, body) {
        var result = "";
        var code = resObj["statusCode"];
        result += "HTTP/1.1 " + resObj["statusCode"] + " " + response.codes[code] + "\n";
        for (var header in resObj["headers"]) {
            result += header + ":" + resObj["headers"]["header"] + "\r\n";
        }
        for (var cookie in resObj["cookies"]){
            result += "Set-Cookie: " + cookie + "=" + resObj["cookies"][cookie] + ";\r\n";
        }
        result += "\r\n" + body +"\r\n";
        return result;
    },

    codes: {
        200: "OK",
        404: "Not Found",
        500: "Server Error"
    },
    createResponse: function(socket){

        var resObj = {};
        resObj["statusCode"] = "";
        resObj["headers"] = {};
        resObj["set"] = function(headerName, headerVal) {
            resObj["headers"][headerName] = headerVal;
        };

        resObj["status"] = function(status) {
            resObj["statusCode"] = status;
            return this;
        };

        resObj["get"] = function(headerName) {
            return resObj["headers"][headerName];
        };

        resObj["cookies"] = {};
        resObj["cookie"] = function(name, value) {
            resObj["cookies"][name] = value;
        };

        resObj["send"] = function(body) {
            var stringRes = response.resToString(resObj, body);
            if (!socket.destroyed) {
                socket.write(stringRes);
                socket.end();
            }
        };

        resObj["json"] = function(bodyToSend) {
            resObj["headers"]["Content-Type"] = "application/json";
            resObj.send(JSON.stringify(bodyToSend));
        };

        return resObj;
    }
};

module.exports = response;
