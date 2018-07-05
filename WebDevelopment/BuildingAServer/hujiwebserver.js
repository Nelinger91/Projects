var net = require('net');
var UrlPattern = require('url-pattern');
var response = require('./response.js');
var request = require('./request.js');

// Consts:
var SOCKET_DELAY = 25000;
var MW_DELAY = 10000;
var MSG_404 = "Not Found";
var MSG_500 = "Server Error";

hujiwebserver = {
    matchCommand: function(req, beginIndex){
        if (beginIndex == -1)
        {
            return [null, -1];
        }
        for (var i = beginIndex; i < this.commands.length; ++i)
        {
            var com = this.commands[i].command;
         try {
             var patt = new UrlPattern(com);
         } catch(err) {
             console.log("quarterpita");
             console.log(err);
         }
            var match = patt.match(req["path"]);
            if (match != null) {
                req.setParams(match);
                return [this.commands[i].middleware, i+1];
            }
        }
        return [null, -1];
    },

    commands:[],
    use: function(command,mw) {
        if(mw == undefined) {
            mw = command;
            command = "/";
        }
        this.commands.push( {
            command:command,
            middleware:mw
        });
        return this;
    },

    start :function(port, callback) {
        var server = net.createServer(function (socket) { //Upon new connection:
            socket.writeable = true;
            var res = response.createResponse(socket);
            var req;
            var endPattern = new RegExp("[\r]+");  // todo improve pattern
            var httpRequest = "";
            socket.on("end", function(err) {
                var res = response.createResponse(socket);
                res.status(500).send(err);
            });
            socket.on("data", function (data) {
                try {
                    httpRequest += data;
                    if (endPattern.test(httpRequest)) {
                        req = request.createRequest(httpRequest);
                    }
                } catch (err) {
                    if (!socket.destroyed) {
                        console.log(err);
                        res = response.createResponse(socket);
                        res.status(500).send(MSG_500);
                    }
                }
                try {
                    var beginIndex = 0;
                    var next = function() {
                        while (mw != null){
                            setTimeout(function(){
                            res.status(404).send(MSG_404);
                            },MW_DELAY);
                            var result = this.matchCommand(req, beginIndex);
                            var mw = result[0];
                            beginIndex = result[1];
                            if (mw == null)
                            {
                                res.status(404).send(MSG_404);
                            }
                            else{
                                mw(req,res,next);
                            }
                        }
                        // if we got here we didn't find a mw
                        var res = response.createResponse(socket);
                        res.status(404).send(MSG_404);
                    };
                    // the start of the command matching. 
                    // iterate "commands" and find a match between the request params and a middleware// result = [mw,beginIndex]
                    var result = hujiwebserver.matchCommand(req,0);
                    var mw = result[0];
                    beginIndex = result[1];
                    if (mw  == null) {
                        res = response.createResponse(socket);
                        res.status(404).send(MSG_404);
                    }
                    else
                    {
                        setTimeout(function(){
                            if (!socket.destroyed) {
                                res = response.createResponse(socket);
                                res.status(404).send(MSG_404);
                            }
                        },MW_DELAY);
                        mw(req,res,next)
                    }    
                    // res = undefined;
                    // req = undefined;
                
                } catch (err) {
                    //console.log(err);
                    if (!socket.destroyed) {
                        res = response.createResponse(socket);
                        res.status(404).send(MSG_404);
                    }
                }
            });

        });

        server.on("connection", function(socket){
            setTimeout(function(){
                var res = response.createResponse(socket);
                res.status(404).send("Not Found");
            },SOCKET_DELAY);
        });

        server.on("error", function(err) {
            if (callback !== undefined){
                callback(err);
            }
        });


        server.listen(port, "localhost");

        serverObj = {
            port: port,
            stop: function() {
                server.close()}
        };
        return serverObj;
    }

};

module.exports = hujiwebserver;
