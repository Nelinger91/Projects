var querystring = require('querystring');

module.exports = {
    createRequest: function(reqString) {
        var reqObj = {};

        var lines = reqString.split("\n");
        var splitFirstLine = lines[0].split(" ");

        reqObj["params"] = {};
        reqObj["path"] = splitFirstLine[1];
        reqObj["query"] = querystring.parse(reqObj["path"]);
        reqObj["method"] = splitFirstLine[0];
        reqObj["protocol"] = splitFirstLine[2].split("/")[0].toLowerCase();
        reqObj["body"] = null;

        var hostPattern = new RegExp("Host:");
        var cookiesPattern = new RegExp("Cookie:");
        var contentTypePattern = new RegExp("Content-Type");
        var contentTypeHeader;

        reqObj["cookies"] = {};
        reqObj["host"] = "";
        flag = false;
        for (var line in lines) {
            if (flag)
            {
                reqObj["body"] += line;
            }
            if (hostPattern.test(line)) {
                reqObj["host"] = line.split(" ")[1];
            }
            if (cookiesPattern.test(line)) {
                var cookiesArray = line.split(":")[1].split(";");
                for (cookie in cookiesArray) {
                    var splittedCookie = cookie.split("=");
                    var name = splittedCookie[0].trim();
                    var value = splittedCookie[1].trim();
                    reqObj["cookies"]["name"] = value;
                }
            }
            if (contentTypePattern.test(line)) {
                contentTypeHeader = line;
            }

            if (line == "\n"){
                flag = true;
            }
        }

        reqObj["setParams"] = function(matches)
        {
            reqObj["params"] = matches;
        };

        reqObj["get"] = function (field) {
            var fieldPattern = new RegExp(field);
            for (var line in lines) {
                if (fieldPattern.test(line)) {
                    return line.split(" ")[1];
                }
            }
        };

        reqObj["param"] = function (param) {
            return params[param];
        };

        reqObj["is"] = function (type) {
            if (contentTypeHeader.indexOf(type) !== -1) {
                return true;
            }
        };

        return reqObj;
    }
};

