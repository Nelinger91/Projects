

var myHTTPserver = require('./hujiwebserver');




// The add command
myHTTPserver.use('/add/:n/:m', function(rq,rs){ rs.json(parseInt(rq.params.n) + parseInt(rq.params.m))}).start(8080);

// the hello world command

myHTTPserver.use('/hello/world', function(rq,rs){ rs.send("hello world")}).start(8080);

//
